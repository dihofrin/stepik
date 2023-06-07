"""
https://stepik.org/lesson/906773/step/12?unit=912312

Класс NonNegativeObject
Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов, причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

Примечание 1. Числами будем считать экземпляры классов int и float.
"""

class NonNegativeObject:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, float | int):
                self.__dict__[k] = abs(v)
            else:
                self.__dict__[k] = v

persons = [('Laura', 'Sawyer', 'elizabethmcneil@example.org', 35), ('Jason', 'Coleman', 'lisareid@example.org', 14),
           ('Joseph', 'Estrada', 'brownwendy@example.net', -13), ('Brian', 'Wood', 'jordancarpenter@example.net', -27),
           ('Michael', 'Higgins', 'masonjennifer@example.com', 12),
           ('Richard', 'Schneider', 'sharonallen@example.com', -30), ('Matthew', 'Jones', 'iterrell@example.net', 15),
           ('Andrew', 'Howard', 'dannymontgomery@example.org', -29), ('Kenneth', 'Myers', 'ftodd@example.net', -20),
           ('Rita', 'Mcdonald', 'christopher25@example.com', 4), ('Cristian', 'Bryant', 'maryjohnson@example.net', 35),
           ('Ashley', 'Dickson', 'johnsoncarly@example.org', 0), ('Mario', 'White', 'anthonynicholas@example.org', -30),
           ('Gregory', 'Curtis', 'lucas53@example.com', 23), ('Daniel', 'Mitchell', 'elizabeth13@example.org', -18),
           ('Michael', 'Chase', 'eric03@example.com', -26), ('Kimberly', 'Burch', 'kcharles@example.com', 10),
           ('Kristen', 'Rollins', 'oliviadunn@example.net', -9),
           ('Sharon', 'Gentry', 'anthonystephens@example.org', -9), ('Joseph', 'Mcmahon', 'lmayer@example.org', 15),
           ('Steven', 'Rhodes', 'christopher82@example.net', -8), ('Joshua', 'Gray', 'lmorales@example.net', 25),
           ('Stephanie', 'Green', 'andersontammie@example.com', -16), ('April', 'Cowan', 'nicolewade@example.net', -12),
           ('Erica', 'Gilmore', 'hubbardsusan@example.org', -31),
           ('Elizabeth', 'Holmes', 'codyrussell@example.com', -38), ('Joseph', 'Campbell', 'kaylee62@example.com', 14),
           ('Jeremy', 'Moore', 'dawsonsean@example.com', -15), ('Monique', 'Crosby', 'michaeljones@example.net', -26),
           ('James', 'Castaneda', 'jonesbarbara@example.org', 28), ('Ryan', 'Glass', 'stephencollins@example.com', -36),
           ('Ryan', 'Holloway', 'jason03@example.com', -10), ('Danielle', 'Allison', 'scottgarcia@example.com', 21),
           ('David', 'Rodriguez', 'edwin89@example.org', 3), ('Fernando', 'Hendrix', 'umccann@example.com', -32),
           ('Elizabeth', 'Herrera', 'christopherhawkins@example.org', -8),
           ('Pamela', 'Davis', 'mariacross@example.com', -38), ('Cynthia', 'Johnson', 'grahamjeremy@example.com', -10),
           ('Christine', 'Stanley', 'kaylafernandez@example.net', -38),
           ('Robert', 'Shelton', 'russelljennifer@example.com', 34),
           ('Brett', 'Wells', 'castrotravis@example.net', -12), ('Nichole', 'Duran', 'wrightanne@example.com', -10),
           ('Ruben', 'Stone', 'angelica95@example.org', -12), ('Daryl', 'Miller', 'hernandezkimberly@example.com', 13),
           ('Megan', 'Wilson', 'garciakathleen@example.net', 31),
           ('Alisha', 'Johnson', 'danielsanchez@example.net', -2), ('Jeffrey', 'Pierce', 'isnyder@example.com', -21),
           ('James', 'Shaffer', 'hailey46@example.net', -4), ('David', 'James', 'janetlee@example.net', 3),
           ('William', 'Kennedy', 'sarahhogan@example.com', 18), ('Kristin', 'Williams', 'marialopez@example.net', -17),
           ('Mark', 'Stevens', 'greenandrea@example.org', 13), ('Earl', 'Thompson', 'dvillanueva@example.org', -34),
           ('Steven', 'Clark', 'scannon@example.com', -22), ('Dennis', 'Schultz', 'anthonythompson@example.org', 1),
           ('Frank', 'Stewart', 'gonzalezjonathan@example.com', 8), ('Matthew', 'Shaffer', 'kevin84@example.org', 33),
           ('Dawn', 'Bradshaw', 'jamesjohnson@example.com', 7), ('Victoria', 'Thomas', 'oyang@example.com', 6),
           ('Brandy', 'Whitehead', 'allenkelly@example.com', -10), ('April', 'Kelly', 'james39@example.com', 19),
           ('Sandra', 'White', 'nicholas66@example.net', 15), ('John', 'Richardson', 'roythomas@example.net', -4),
           ('Bryan', 'Walker', 'crossfernando@example.com', 26), ('John', 'Martin', 'linda33@example.com', 25),
           ('Bryan', 'Ford', 'monica03@example.com', 25), ('Kimberly', 'Nguyen', 'jeffrey30@example.org', -3),
           ('Robin', 'Clark', 'ybishop@example.com', -12), ('Eric', 'Hoffman', 'tammyhanson@example.com', -21),
           ('Sarah', 'Lopez', 'qortiz@example.net', -11), ('Eileen', 'Garcia', 'leroy26@example.org', -11),
           ('Danny', 'Harrison', 'danavelez@example.com', 9), ('Andrew', 'Martin', 'frussell@example.net', 7),
           ('Jennifer', 'Aguilar', 'xallen@example.org', -39),
           ('Michelle', 'Johnson', 'andrewilliams@example.org', -26),
           ('Dennis', 'Mercado', 'sheilaharrison@example.net', -8),
           ('Rebecca', 'Lara', 'matthewnavarro@example.org', 30),
           ('Sarah', 'Joseph', 'frederickzachary@example.net', -18),
           ('John', 'Butler', 'pachecochristina@example.org', 25), ('Laura', 'Hunter', 'devincruz@example.com', 6),
           ('Kenneth', 'Carr', 'collierscott@example.net', -25), ('Amy', 'Estrada', 'tina18@example.com', 16),
           ('Cameron', 'Jackson', 'laurasnyder@example.com', 13),
           ('Debbie', 'Sullivan', 'taracochran@example.com', -16), ('Kelsey', 'Norris', 'duane84@example.com', 28),
           ('Timothy', 'Marks', 'peterlawson@example.net', -37), ('Monique', 'Carroll', 'jeremy81@example.org', 11),
           ('Matthew', 'Mathews', 'stephen36@example.org', 30), ('Jackie', 'Kim', 'justincantrell@example.com', -24),
           ('Kathy', 'Jones', 'nyates@example.com', -5), ('Amber', 'Hunter', 'leeelizabeth@example.com', -8),
           ('Lauren', 'Peters', 'willieprice@example.org', -23), ('Donald', 'Anderson', 'khowell@example.net', -20),
           ('Jessica', 'Moreno', 'mfrank@example.net', -23), ('Hailey', 'Golden', 'gjohnson@example.net', 33),
           ('Matthew', 'Williams', 'murraynancy@example.net', 26),
           ('Gina', 'Montoya', 'collinsricardo@example.net', 26), ('Michael', 'Carroll', 'jwarren@example.com', -34),
           ('Jacob', 'Lopez', 'juliegarcia@example.com', 40),
           ('Vanessa', 'Blackwell', 'gordonadrienne@example.com', -38)]

for name, surname, email, age in persons:
    person = NonNegativeObject(name=name, age=age, email=email, surname=surname)
    print(person.name, person.surname, person.email, person.age)