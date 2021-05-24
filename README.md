# Simple web app to provide an API to the valuation model developed for the VOA Data Project



### Example Usage



`import requests`
`import json`

`url = 'https://voa-model-api.herokuapp.com/voa-api/'`
`data = [[1055.0, 302.5, 249.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,` 
         `0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7570247933884298, 0.0,` 
         `0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.22016528925619833, 0.0228099173553719, 0.0, 0.0,` 
         `0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,` 
         `0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]`
`json_data = json.dumps(data)`
`headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}`
`r = requests.post(url, data=json_data, headers=headers)`
`print(r.text)`



Yields a dictionary with two keys: 'predicted_rv' and 'shap_values':

```
{"predicted_rv":"68.27991494","shap_values":{"AirConditioningSystemPct":-5.306942063974761,"AllMainAreasPct":-0.03446747378651801,"AreaUnderSupportedFloorPct":-0.0061089558567267565,"BarPct":-0.0004821223467996418,"BillingAuthorityCode":-32.00895246951492,"CPSpaces":-0.4576341188728618,"CanteenPct":0.0005043063061403403,"ChillStorePct":-0.005704371562293244,"ClassroomPct":0.0,"ColdStorePct":0.00035715469893517974,"ComputerRoomPct":0.00030918831520750176,"ExternalStoragePct":0.7212195578930345,"FirstFloorSalesPct":0.0,"GaragePct":0.11911436073779468,"GolfCoursePct":-0.06497364387504986,"GroundFirstOrSecondPct":1.514436257888296,"GroundFloorSalesPct":-2.639692352477138,"HallPct":0.0012519436785284944,"HardSurfacedFencedLand_02Pct":0.0014905616961751245,"HardSurfacedFencedLand_03Pct":-0.0677938844545953,"HardSurfacedUnfencedLandPct":-0.010431078911099623,"IndoorArenaPct":-0.12650487472057867,"InternalStoragePct":9.39191960101194,"KitchenPct":1.468289174695306,"LaboratoryPct":-0.02289867255673171,"LoungePct":0.000310397467651,"MessStaffRoomPct":-0.2686053256708588,"MezzanineFloorPct":-0.04157512876337754,"MiscellaneousAdditionPct":-0.02256200719194232,"NurseryPct":-0.0018700217736579976,"Office_02Pct":-24.15531784995338,"Office_03Pct":-0.13495297380580737,"OtherDescriptionPct":0.00977760431214137,"OtherFloorPct":-4.176480699832339,"OtherOADescriptionPct":-0.29247987733688346,"OutdoorArenaPct":-0.2224576565104443,"ParkingSpaceSPct":-0.30336622646903344,"PetrolForecourtandShopPct":0.0,"PortableBuildingPct":-0.019624613740219024,"ProductionAreaPct":0.031092560151921137,"ReceptionEntrancePct":-0.17008044096267808,"RemainingRetailZonePct":-0.5755623837701395,"RestaurantPct":-0.13735625522871692,"RetailAreaPct":-0.5166823849755398,"RetailZoneAPct":-11.268108228928297,"RetailZoneBPct":-2.630059331992407,"RetailZoneCPct":-3.9665451356314607,"RoughSurfacedFencedLand_02Pct":0.00019585084643723884,"RoughSurfacedFencedLand_03Pct":-0.03108540353647005,"SCATCodeOnly":-7.914659912485665,"ShowroomPct":-0.018294508775925686,"SingleBedSpacePct":-0.10441439962979027,"StorageContainerPct":-0.002888959193362036,"StorePct":0.35137723278930855,"Store_03Pct":-0.15760927297612345,"SupportedStorageFloorPct":-0.018368003876955304,"SurgeryPct":-0.02802089067312618,"TotalArea":-25.195087053821187,"TotalFloorAreaDryLeisureClubsPct":-0.0009058521403709874,"UnitofMeasurement_Int":-1.059231605195044,"UnsurfacedFencedLand_02Pct":0.0,"UnsurfacedFencedLand_03Pct":-0.023764870422870607,"UnsurfacedUnfencedLandPct":-0.0009097037883985033,"VehicleDisplaySpacesPct":-0.029459986055298547,"VehicleSpacesPct":-0.002193061039818842,"WarehousePct":0.03543518035079309,"WorksOfficePct":-0.00021165502696101897,"Workshop_02Pct":1.0419664535275088,"Workshop_03Pct":-0.01327820289369808}}
```

More information about the underlying data and the modelling process can be found in [here](https://github.com/pasbury/voa-data-project).



