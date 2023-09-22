import uuid
import os
import subprocess
from languages import languages
from codes import get_code


def prepare_file(id, code, language, parameters, func, test):
    os.mkdir(id, 0o755)
    extension = languages[language]['extension']
    code_string = get_code(language, code, func, parameters)
    with open(f'{id}/test{extension}', 'w') as file:
        file.write(code_string)
    os.system(f'cp tests/{test} {id}/test.json')
    os.system(f'chmod 0555 {id}/test{extension}')


def prepare_docker(id, language):
    with open(f'{id}/Dockerfile', 'w') as file:
        docker_image = languages[language]['docker-image']
        file.write(f'FROM {docker_image}\n\n')
        extension = languages[language]['extension']
        file.write(f'COPY test{extension} test.json ./\n\n')
        command = languages[language]['cmd']
        file.write(f'CMD {command}')


def run_code(parameters):
    id = str(uuid.uuid4()) # uuid4 generates a random UUID
    code = parameters['code'].replace('\t', '    ')
    language = parameters['language']
    params = parameters['params']
    func = parameters['func']
    test = parameters['test']

    try:
        prepare_file(id, code, language, params, func, test)
        prepare_docker(id, language)
        subprocess.run(['docker', 'build', '-t', id, id])
        run = subprocess.run(
            ['docker', 'run', '-t', id],
            stdout=subprocess.PIPE,
            timeout=5
        )
        print('Run:', run.stdout.decode('utf-8'))
        error = False
        output = ''
        if run.returncode:
            error = True
            output = 'Error'
        else:
            stdout = run.stdout.decode('utf-8').replace('\r', '')
            output = stdout.split('\n')[:-1]
    except subprocess.TimeoutExpired:
        error = True
        output = 'Timeout Exceeded'
    except Exception as e:
        error = True
        output = [str(type(e).__name__), str(e), 'Error']
    finally:
        return {
            'Error': error,
            'Output': output,
        }