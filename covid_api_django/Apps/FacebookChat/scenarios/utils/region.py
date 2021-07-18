def get_country(content):
    return content['postback']['payload'].split('_')[-2]


def get_country_list(continent: str,
                     countries: dict,
                     page: int,
                     offset: int = 10):
    ret = list(map(
        lambda country: {
            "content_type": "text",
            "title": "{countryName}".format(countryName=country['name']),
            "payload": "sub_{continent}_{countryCode}_{pageNum}"
                .format(continent=continent, countryCode=country['code'], pageNum=page)
        },
        countries[continent][(page - 1) * offset:page * offset]
    ))

    if page > 1:
        ret.insert(0, {
            "content_type": "text",
            "title": "prev",
            "payload": "sub_{continent}_{pageNum}".format(continent=continent, pageNum=page - 1)
        })

    if page <= len(countries[continent]) // offset:
        ret.append({
            "content_type": "text",
            "title": "next",
            "payload": "sub_{continent}_{pageNum}".format(continent=continent, pageNum=page + 1)
        })

    return ret


if __name__ == '__main__':
    ...
