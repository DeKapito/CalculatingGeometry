# Лабораторна робота №3
## Приклади виконання
### Завдання 1
#### Скласти процедуру для розрахунку вершин сітки, яка наближено передає форму пісочного годинника (кількість вершин не менше 20). Бажано, щоб сітка утворювалась приблизно рівними за площею трикутниками або чотирикутниками. 

### Завдання 2
#### Скласти процедуру для з’єднання вершин каркасу фігури. Для скорочення алгоритму велику роль відіграє добре продумана нумерація та порядок з’єднання вершин, щоб якомога більше використати цикли. 


Вершини пісочного годинника формуються пошарово, тобто малюються вершини одного кола, потім іншого з іншим радіусом та на іншій висоті і т.д. В кожному кільці міститься 10 вершин, кілець 10, отже дана фігура містить 100 вершин. Кількість вершин в кільці дуже легко змінити за допомогою поля self.num_vertexes

Фрагмент коду побудови вершин:

```python
angle_step = 2 * math.pi / self.num_vertexes
vertexes = []
for height, radius in zip(self.heights, self.radiuses):
    for i in range(0, self.num_vertexes):
        vertex = Vertex()
        vertex.x = math.cos(i * angle_step) * radius
        vertex.y = math.sin(i * angle_step) * radius
        vertex.z = height
        vertexes.append(vertex)
```
Фрагмент коду малювання каркасу (кожен шар з'єднується з наступним):

```python
for i in range(1, len(points[0])+1):     
    source = i - 1
    target = i
    if i % self.num_vertexes == 0:
        target = i - self.num_vertexes
    self.draw_line(
        points[0][source], points[1][source],
        points[0][target], points[1][target],
        color=color
    )
    if i < len(points[0]) - self.num_vertexes:
        self.draw_line(
            points[0][source], points[1][source],
            points[0][source+self.num_vertexes], points[1][source+self.num_vertexes],
            color=color
        )
    if i % self.num_vertexes == 0:
        color = next(colors)
```

Проекція фігури на площину xOy
![xOy](https://raw.githubusercontent.com/DeKapito/CalculatingGeometry/master/lab3/screenshots/xOy.PNG)

Проекція фігури на площину xOz
![xOz](https://raw.githubusercontent.com/DeKapito/CalculatingGeometry/master/lab3/screenshots/xOz.PNG)

Проекція фігури на площину yOz
![yOz](https://raw.githubusercontent.com/DeKapito/CalculatingGeometry/master/lab3/screenshots/yOz.PNG)

Диметрична проекція
![dimetric](https://raw.githubusercontent.com/DeKapito/CalculatingGeometry/master/lab3/screenshots/dimetric.PNG)

Анімація диметричної проекції (для більшої наочності)
![dimetric_animation](https://raw.githubusercontent.com/DeKapito/CalculatingGeometry/master/lab3/screenshots/dimetric_animation.gif)
