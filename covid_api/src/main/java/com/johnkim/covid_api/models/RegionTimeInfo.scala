package com.johnkim.covid_api.models

import com.fasterxml.jackson.annotation.JsonIgnoreProperties
import com.johnkim.covid_api.models.regionDetails.
  {ARIMAPredictionInfo, CSSECovidCases, GoogleMobilityInfo, OWIDPScoresInfo, OWIDRegionDetailInfo, OWIDTestingInfo, OWIDVaccinationInfo}

@JsonIgnoreProperties(ignoreUnknown = true)
class RegionTimeInfo {
  var csseCovidCases: CSSECovidCases = _

  var arimaPredictionInfo: ARIMAPredictionInfo = _

  var owidRegionDetailInfo: OWIDRegionDetailInfo = _
  var owidTestingInfo: OWIDTestingInfo = _
  var owidVaccinationInfo: OWIDVaccinationInfo = _
  var owidPScoresInfo: OWIDPScoresInfo = _

  var googleMobilityInfo: GoogleMobilityInfo = _

}
