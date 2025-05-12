import pandas as pd

def pregunta_01():
  with open('files/input/clusters_report.txt') as file:
    lines = file.read()

  lines = lines.replace('.', '')
  lines = lines.split('\n')

  columns1 = lines[0].strip().replace(' ', '_')
  columns2 = lines[1].ljust(len(columns1), '_').replace(' ', '_')

  mayusculas = []
  for letter in columns1:
    if letter.isupper():
      mayusculas.append(letter)
  for letter in list(set(mayusculas)):
    columns1 = columns1.replace(letter, f'¿{letter}')
  columns1 = columns1.split('¿')
  col = []
  for word in columns1:
    if word == '':
      continue
    col.append(word)
  start = 0
  columns = []
  for i in range(len(col)):
    end = start + len(col[i])
    columns.append(col[i] + columns2[start:end])
    start = end
  columns = list(map(lambda x: '_'.join([parte for parte in x.strip('_').lower().split('_') if parte != '']), columns))

  data = {key: [] for key in columns}
  cont = -1
  for line in lines[4:]:
    split_line = line.split()
    if len(line.split()) == 0:
      continue
    if split_line[0].isdigit():
      cont += 1
      data[columns[0]].append(int(split_line[0]))
      data[columns[1]].append(int(split_line[1]))
      data[columns[2]].append(float(split_line[2].replace(',','.')))
      data[columns[3]].append('')
      clave = ' '.join(split_line[4:])
    else:
      clave = ' ' + ' '.join(split_line)
    data[columns[3]][cont] += clave
  return pd.DataFrame(data = data)