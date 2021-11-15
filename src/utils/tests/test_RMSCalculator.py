from src.utils.RMSCalculator import calculate_rms


def test_if_rms_calculator_works():
    foo = [
        0.0,
        1.1879507853809015,
        3.733559611197119,
        1.697072550544145,
        0.7636826477448653,
        1.4425116679625236,
        3.,
        6.78829020217658,
        11.45523971617298,
        14.509970307152443,
        4.836656769050814,
        - 1.4425116679625236,
        - 1.4425116679625236,
        - 1.3576580404353162,
        - 1.3576580404353162,
        - 1.2728044129081089,
        - 1.2728044129081089,
        - 1.1879507853809015,
        - 1.1030971578536943,
        - 1.1030971578536943,
        - 0.8485362752720725,
        - 1.2728044129081089,
        - 2.7153160808706325,
        - 2.9698769634522537,
        - 0.9333899027992798,
        - 0.6788290202176581,
        - 2.5456088258162177,
        - 3.563852356142705,
        - 4.32753500388757,
        - 13.067458639189917,
        - 14.849384817261273,
        - 10.182435303264871,
        1.8667798055985596,
        1.8667798055985596,
        0.8485362752720725,
        0.0
    ]
    result = calculate_rms(foo)
    # print(f'\n{calculate_rms(foo)}')
    assert result == 5.313693327771444
