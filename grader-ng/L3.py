# coding: utf-8

def pau_header(cell):
    return cell[0] == 'TOTAL'

def pau_footer(cell):
    return cell[0] == ''

def csv_extractor(path, row_extractor,
                  header_condition = pau_header,
                  footer_condition = pau_footer):
    ret = []
    with open(path,'r') as f:
        header = True
        for row in f:
            cell = row.strip().split(',')
            if not header:
                if footer_condition(cell):
                    break
                ret.append(row_extractor(cell))
            elif header_condition(cell):
                header = False
    return ret


def get_column_0(cell):
    return cell[0]

def comunidades_autonomas(path):
    ret = csv_extractor(path, get_column_0)
    return sorted(ret)

def get_column_0_

def aprobados_pau(path):
    return { d[0]:d[1] for d in csv_extractor(path, get_columns_0_x) }


def suspensos_pau():
    pass


def comunidad_mas_aprobados():
    pass


def comunidad_mas_diferencia():
    pass


print comunidades_autonomas('tests/pcaxis637310428.csv')
