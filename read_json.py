import json
import re


def main():
    # json_datas = read_json_data('Industry Maintenance', "industry")
    # for json_data in json_datas:
    #     print(json_data['compname'])
    button_components = read_button_components_json("add")
    for button_component in button_components:
        print(button_component['compname'])
    # print(button_components)


def read_json_data(settings_form, input_field_name):
    settings_form = re.sub(r'[^a-zA-Z0-9]+', '_', settings_form).strip('_')
    settings_form = settings_form.lower()
    with open('settings/component_names.json') as json_file:
        datas = json.load(json_file)

    json_outputs = []
    for data in datas['settings']:
        if settings_form in data:
            for component in data[settings_form]:
                if input_field_name in component:
                    json_outputs.append(component[input_field_name])

    return json_outputs


def read_button_components_json(button_name):
    with open('settings/button_components.json') as json_file:
        button_components = json.load(json_file)

    button_compnames = button_components.get('buttons', [])
    buttons = None

    for button_component in button_compnames:
        buttons = button_component.get(f'{button_name}', [])

    return buttons


if __name__ == "__main__":
    main()
