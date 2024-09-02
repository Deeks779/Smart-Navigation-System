import ipywidgets
select_widget=ipywidgets.Select(
    options=['Option A', 'Option B'],
    value='Option A',
    description='Select',
    disabled=False)

def selectOption(opt):
    if opt == 'Option A':
        print('A')
    if opt == 'Option B':
        print('B')

ipywidgets.interact(selectOption, opt=select_widget)
