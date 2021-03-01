package com.johnkim.covid_api.models

import com.fasterxml.jackson.annotation.JsonIgnoreProperties

@JsonIgnoreProperties(ignoreUnknown = true)
class RegionMetaInfo {
  var continent: String = _

  var country: String = _
  var countryCode: String = _

  var subRegionFrom: String = _
  var subRegionPath: String = _

}




















