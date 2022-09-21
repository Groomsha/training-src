# Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор,
# который будет оставлять в последовательности только чётные числа.

import json
import pickle


if __name__ == '__main__':
	shop_dict = {
		"Status": 1,
		"Category": {
			"Id": 5450,
			"ExternalId": 6686,
			"ParentId": 6685,
			"RootId": 316,
			"Type": "catalog",
			"ShortName": "",
			"DescriptionRu": "да",
			"DescriptionUa": "Сервера",
			"TaglineRu": "",
			"TaglineUa": "",
			"RobotsRu": "",
			"RobotsUa": "",
			"SlugRu": "Servera-c6686",
			"SlugUa": "Servera-c6686",
			"Changefreq": "",
			"Priority": "",
			"Status": "active",
			"IsRu": True,
			"IsUa": True,
			"ForAuth": True,
			"ForAnonymous": True,
			"Comment": "",
			"MainPageUrl": "",
			"ClassCode": "K0036",
			"IsMain": False,
			"CatalogType": "main",
			"ManualPriority": 1,
			"CategoryType": "default",
			"StartTime": None,
			"FinishTime": None,
			"Picture": "https://img7.itbox.ua/150x150/prod_img/7/U0621947.jpg",
			"RedirectId": None,
			"CommonPriority": None,
			"CustomMultlistNameUa": None,
			"CustomMultlistNameRu": None,
			"MultlistTitleUa": None,
			"MultlistTitleRu": None,
			"MultlistFilterNameUa": None,
			"MultlistFilterNameRu": None,
			"ShowMultlistNestedCatalogs": False,
			"IsBackbuy": 0,
			"AddTime": "2021-09-18 14:00:17",
			"UpdateTime": None,
			"ChildrenLastMod": None,
			"MetaUaLastMod": None,
			"MetaRuLastMod": None,
			"Name": "Серверы",
			"Slug": "Servera-c6686",
			"PageTitle": "Серверы ᐈ Купить сервер в Киеве недорого - цены на Серверы | ITbox.ua",
			"MetaName": "Серверы ᐈ Купить сервер в Киеве недорого - цены на Серверы | ITbox.ua",
			"ShowParent": False,
			"MetaDescription": "Серверы в интернет-магазине ITbox от 35958 грн. ⏩ Кэшбек ⚡ Низкие цены ✨",
			"MultlistTitle": None,
			"MultlistFilterName": None,
			"ParentName": "",
			"AllClassCodes": ["K0036"]
		},
	}

	with open('shop.json', 'wb') as file:
		pickle.dump(json.dumps(shop_dict, indent=2, ensure_ascii=False), file)
