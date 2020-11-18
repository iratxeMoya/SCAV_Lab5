from PyInquirer import prompt

def mainMenu():
    menuOpts = [
        {
            'type': 'list',
            'name': 'Action menu',
            'message': 'Select wanted action',
            'choices': [
                'Parse ffmpeg',
                'Rename',
                'Resize',
                'Change codec'

            ]
        }
    ]

    return prompt(menuOpts)

def videoNameMenu():
    menuOpts = [
        {
            'type': 'input',
            'name': 'video file',
            'message': 'Introduce video path'
        }
    ]

    return prompt(menuOpts)

def renameMenu():
    menuOpts = [
        {
            'type': 'input',
            'name': 'rename',
            'message': 'Introduce new name for file'
        }
    ]

    return prompt(menuOpts)

def sizeMenu():
    menuOpts = [
        {
            'type': 'input',
            'name': 'width',
            'message': 'Introduce width for resizing'
        },
        {
            'type': 'input',
            'name': 'height',
            'message': 'Introduce height for resizing'
        }
    ]

    return prompt(menuOpts)