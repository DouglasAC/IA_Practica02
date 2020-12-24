model2 = Model(train_set, test_set, reg=True, alpha=0.0001, lam=300) #Baja más quitandole la regularización

Eficacia en entrenamiento:  95.46925566343042
Eficacia en prueba:  92.4812030075188
model2 = Model(train_set, test_set, reg=False, alpha=0.0001, lam=300) #Baja más quitandole la regularización
Eficacia en entrenamiento:  94.8220064724919
Eficacia en prueba:  90.22556390977444
------------
model2 = Model(train_set, test_set, reg=True, alpha=0.0001, lam=450) #Baja más quitandole la regularización
Eficacia en entrenamiento:  96.11650485436893
Eficacia en prueba:  90.22556390977444
------------
 model2 = Model(train_set, test_set, reg=False, alpha=0.000001, lam=450) #Baja más quitandole la regularización
 Eficacia en entrenamiento:  84.14239482200648
Eficacia en prueba:  81.95488721804512
------------
model2 = Model(train_set, test_set, reg=False, alpha=0.00001, lam=450) #Baja más quitandole la regularización

Eficacia en entrenamiento:  93.20388349514563
Eficacia en prueba:  87.21804511278195
------------
200000
model2 = Model(train_set, test_set, reg=False, alpha=0.00001, lam=450) #Baja más quitandole la regularización
Eficacia en entrenamiento:  93.85113268608414
Eficacia en prueba:  90.97744360902256
------------