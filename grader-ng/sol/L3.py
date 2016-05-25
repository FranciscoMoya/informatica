# coding: utf-8

def pau_header(cells):
    return cells[0] == 'TOTAL'

def pau_footer(cells):
    return cells[0] == ''

def csv_extractor(path, row_extractor,
                  header_condition = pau_header,
                  footer_condition = pau_footer):
    ret = []
    with open(path,'r') as f:
        header = True
        for row in f:
            cells = row.strip().split(',')
            if not header:
                if footer_condition(cells):
                    break
                ret.append(row_extractor(cells))
            elif header_condition(cells):
                header = False
    return ret

def get_column_0(cells):
    return cells[0]

def comunidades_autonomas(path):
    ret = csv_extractor(path, get_column_0)
    return sorted(ret)

def get_columns_0_11(cells):
    return (cells[0],value_as_int(cells[11]))

def value_as_int(v):
    return int(value_as_float(v))

def value_as_float(v):
    if v[0] == '"':
        v = v[1:-1]
    return float(v)

def aprobados_pau(path):
    return { d[0]:d[1] for d in csv_extractor(path, get_columns_0_11) }


def get_columns_0_1_minus_11(cells):
    return (cells[0],value_as_int(cells[1]) - value_as_int(cells[11]))


def suspensos_pau(path, comunidad):
    susp = { d[0]:d[1] for d in csv_extractor(path, get_columns_0_1_minus_11) }
    if comunidad in susp:
        return susp[comunidad]
    raise ValueError('No hay datos de ' + comunidad)

def get_columns_0_11_div_into_1(cells):
    return (cells[0],value_as_float(cells[11])/value_as_float(cells[1]))

def column_1(cells):
    return cells[1]

def comunidad_mas_aprobados(path):
    return sorted(csv_extractor(path, get_columns_0_11_div_into_1),
                  key = column_1, reverse=True)[0][0]

def column_1(cells):
    return cells[1]

def get_diff_rate(cells):
    jun = value_as_float(cells[13])/value_as_float(cells[3])
    sep = value_as_float(cells[15])/value_as_float(cells[5])
    return (cells[0], abs(jun-sep))
    
def comunidad_mas_diferencia(path):
    return sorted(csv_extractor(path, get_diff_rate),
                  key = column_1, reverse=True)[0]


if __name__ == '__main__':
    print comunidades_autonomas('tests/pcaxis637310428.csv')
    print aprobados_pau('tests/pcaxis637310428.csv')
    print suspensos_pau('tests/pcaxis637310428.csv', 'Extremadura')
    print suspensos_pau('tests/pcaxis637310428.csv', 'Canarias')
    print comunidad_mas_aprobados('tests/pcaxis637310428.csv')
    print comunidad_mas_diferencia('tests/pcaxis637310428.csv')
