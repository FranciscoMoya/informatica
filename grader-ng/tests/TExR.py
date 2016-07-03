import unittest, sys

try: from lab import imprimir_hex
except: pass

try: from lab import frequent_browsers
except: pass

try: from lab import butterworth
except: pass

try: from lab import pi_leibniz
except: pass

try: from lab import mediana
except: pass

try: from lab import validar_tarjeta
except: pass

epsilon = 0.001

class Test_ExR(unittest.TestCase):

    def setUp(self):
        self.console = sys.stdout
        sys.stdout = open('/tmp/out.txt', 'w')

    def tearDown(self):
        sys.stdout = self.console

        
    def test_imprimir_hex(self):
        self.assertEqual(self.std_output(imprimir_hex(1)),
                         [' _',
                          '/ \\',
                          '\\_/'])
        self.clear_std_output()
        self.assertEqual(self.std_output(imprimir_hex(2)),
                         ['  __',
                          ' /  \\',
                          '/    \\',
                          '\\    /',
                          ' \\__/'])
        self.clear_std_output()
        self.assertEqual(self.std_output(imprimir_hex(4)),
                         ['    ____',
                          '   /    \\',
                          '  /      \\',
                          ' /        \\',
                          '/          \\',
                          '\\          /',
                          ' \\        /',
                          '  \\      /',
                          '   \\____/'])
        self.clear_std_output()

        
    def test_frequent_browsers(self):
        self.assertEqual(frequent_browsers('tests/access.log'), [])
        self.assertEqual(frequent_browsers('tests/access_small.log'),
                         [('Mozilla/4.0 ' \
                           '(compatible; MSIE 6.0; Windows NT 5.2; ' \
                           'WOW64; SV1; .NET CLR 2.0.50727)',
                           6.0)])
        self.assertEqual(frequent_browsers('tests/access_mini.log'),
                         [('Mozilla/5.0 ' \
                           '(Windows NT 6.3; WOW64) ' \
                           'AppleWebKit/537.36 ' \
                           '(KHTML, like Gecko) ' \
                           'Chrome/32.0.1700.102 ' \
                           'Safari/537.36',
                           100.0)])

        
    def test_butterworth(self):
        self.assertTrue(abs(butterworth(.9, .1, 1e3, 2e3)[1]
                            - 1156.0407465973783) < epsilon)
        self.assertEqual(butterworth(.9, .1, 1e3, 2e3)[0], 5)
        self.assertTrue(abs(butterworth(.9, .1, 1e3, 1.1e3)[1]
                            - 1022.9150147595658) < epsilon)
        self.assertEqual(butterworth(.9, .1, 1e3, 1.1e3)[0], 32)
        self.assertTrue(abs(butterworth(.9999, .0001, 1e3, 1.1e3)[1]
                            - 1030.4438056085637) < epsilon)
        self.assertEqual(butterworth(.9999, .0001, 1e3, 1.1e3)[0], 142)


    def test_pi_leibniz(self):
        self.assertTrue(abs(pi_leibniz(1) - 4.) < epsilon)
        self.assertTrue(abs(pi_leibniz(100) - 3.1315929035585537) < epsilon)
        self.assertTrue(abs(pi_leibniz(100000) - 3.14158265359) < epsilon)

    def test_mediana(self):
        self.assertEqual(mediana(range(9)), 4)
        self.assertEqual(mediana(range(10)), 4.5)
        self.assertEqual(mediana([10,2]), 6.)

    def test_validar_tarjeta(self):
        self.assertTrue(validar_tarjeta('4578463073273942'))
        self.assertTrue(validar_tarjeta('5328845898315140'))
        self.assertFalse(validar_tarjeta('4578463073273940'))
        self.assertFalse(validar_tarjeta('5328845898315143'))
        
    def std_output(self, _):
        sys.stdout.flush()
        with open('/tmp/out.txt', 'r') as f:
            return [x.rstrip() for x in f.readlines()]
        
    def clear_std_output(self):
        sys.stdout.truncate(0)
        sys.stdout.seek(0)
