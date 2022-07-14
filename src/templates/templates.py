def make_component_file(component):
    component_file = f"import React from 'react';\
\n\
\r\n\
export interface {component}Props \u007b \u007d\
\n\
\r\n\
const {component}: React.FC<{component}Props> = () => \u007b\n\
  return (\n\
    <div>Hello</div>\n\
  );\n\
\u007d;\
\n\r\
export default {component}; \n"
    return component_file

def make_index_file(component):
    index_file = f"import {component} from './{component}.tsx';\
\n\
\r\n\
export default {component} \n"
    return index_file

def make_test_file(component):
    test_file = f"import \u007b render, userEvent \u007d from 'react-testing-library';\
\n\
\r\n\
import {component} from './{component}.tsx';\
\n\
\r\n\
describe('[{component.upper()}]', () => \u007b\n\
  it('should render correctly', () => \u007b\n\
    const wrapper = render({component});\
\n\
\r\n\
    expect(wrapper.baseElement).toMatchSnapshot();\n\
  );\n\
\u007d);\n"
    return test_file


def default_template(component):
    with open(f'{component}/{component}.tsx', 'w') as file:
        file.write(make_component_file(component))
        file.close()
    with open(f'{component}/index.tsx', 'w') as file:
        file.write(make_index_file(component))
        file.close()
    with open(f'{component}/{component}.test.tsx', 'w') as file:
        file.write(make_test_file(component))
        file.close()

def TemplateFactory(template_name):
    return default_template
