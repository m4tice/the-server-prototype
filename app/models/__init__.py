from . import wz_model

wz_model_instance = wz_model.WzModel("app/models/wz.db")
headers = wz_model_instance.get_headers_alternative()
data = wz_model_instance.get_all_data()
