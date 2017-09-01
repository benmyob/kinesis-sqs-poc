from falsy.falsy import FALSY

f = FALSY()  # you need create the dir called static before you run
f.swagger('spec.yml', ui=True,
          theme='impress')  # impress theme is the responsive swagger ui, or you can use 'normal' here
api = f.api