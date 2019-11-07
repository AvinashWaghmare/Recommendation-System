from django.core.validators import MaxValueValidator
from django.db import models



Gender = (
		(1, 'Male'),
		(0, 'Female'),
)
Cycle_Type = (
		(0,'Kids Bike'),
		(1,'Moutain Bike'),
		(2,'Hybrid/Comfort Bike'),
		(3,'Road Bike'),
		(4,'RiverSide Bike'),
)
Cycle_id = ((4454833,4454833),
(1234590,1234590),
(3454264,3454264),
(4563361,4563361),
(6754535,6754535),
(8094518,8094518),
(3763781,3763781),
(6583190,6583190),
(3453147,3453147),
(8974225,8974225),
(7013035,7013035),
(7024599,7024599),
(2563594,2563594),
(2344971,2344971),
(9741381,9741381),
(5463099,5463099),
(7654545,7654545),
(3543269,3543269),
(6452786,6452786),
(6784484,6784484),
(3493042,3493042),
(1282865,1282865),
(8761061,8761061),
(4534883,4534883),
(4734847,4734847),
(5464484,5464484),
(2534222,2534222),
(6544414,6544414),
(5494239,5494239),
(1541964,1541964),
(6753571,6753571),
(3451847,3451847),
(9451334,9451334),
(7864885,7864885),
(2431831,2431831),
(8764868,8764868),
(4561940,4561940),
(4322491,4322491),
(5674415,5674415),
(4563196,4563196),
(5674461,5674461),
(7893769,7893769),
(6784540,6784540),
(9803389,9803389),
(9083034,9083034),
(8904822,8904822),
(7894993,7894993),
(7893575,7893575)
)


Cycling_Reason = (
		(0,'Playing'),
		(1,'Exercise and Commute'),
		(2,'Exercise and Commute and Lond Distance'),
		(3,'Long Distance'),
		(4,'Commute'),
)



class Cycle(models.Model):
	gender: int = models.PositiveSmallIntegerField(default=0, choices= Gender)
	age: int = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
	cycle_type: int = models.PositiveSmallIntegerField(default=0, choices=Cycle_Type)
	cycling_id: int = models.PositiveSmallIntegerField(choices=Cycle_id)
	cycling_Reason: int = models.PositiveSmallIntegerField(default=0, choices=Cycling_Reason)
	mrp: int = models.PositiveSmallIntegerField(validators=[MaxValueValidator(199999)])


				






			



			

 