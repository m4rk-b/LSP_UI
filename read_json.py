import json
import re


def main():
    # json_datas = read_json_data('Accounting Entity Maintenance', "accounting_entity")
    json_datas = read_admin_comp_json('Accounting Entity Maintenance', 'accounting_entity', 'administration')
    for json_data in json_datas:
        print(json_data['compname'])
        print(json_data['selector'])
        print(json_data['default'])
    # button_components = read_button_components_json("add")
    # for button_component in button_components:
    #     print(button_component['compname'])
    # print(button_components)

def read_admin_comp_json(form_name, input_field_name, menu):
    lsp_form_name = re.sub(r'[^a-zA-Z0-9]+', '_', form_name).strip('_')
    lsp_form_name = lsp_form_name.lower()
    input_field_name = input_field_name.lower()
    with open(f'settings/component_names.json') as json_file:
        datas = json.load(json_file)

    json_outputs = []
    for data in datas[menu]:
        if lsp_form_name in data:
            for component in data[lsp_form_name]:
                if input_field_name in component:
                    json_outputs.append(component[input_field_name])

    return json_outputs

def read_json_data(settings_form, input_field_name):
    settings_form = re.sub(r'[^a-zA-Z0-9]+', '_', settings_form).strip('_')
    settings_form = settings_form.lower()
    with open('settings/component_names.json') as json_file:
        datas = json.load(json_file)

    json_outputs = []
    for data in datas['administration']:
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
