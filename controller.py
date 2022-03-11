import database_scripts


def get_promos():
    return database_scripts.select_promos()


def get_promo(promo_id):
    results = database_scripts.select_promos(promo_id)
    return results


def post_promo(name, description):
    return database_scripts.insert_promo(name, description)
