from girisdogrulama import sifre_guclu_mu

def test_dogru_sifre():
    assert sifre_guclu_mu("Guclu123!") is True

def test_eksik_sifre():
    assert sifre_guclu_mu("guclu123!") is False

def test_hatali_sifre():
    assert sifre_guclu_mu("Guclu123") is False

# python -m pytest ile terminalden test et, run tuşunu kullanma

