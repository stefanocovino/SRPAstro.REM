""" 

Context : SRP
Module  : REM
Version : 1.0.57
Author  : Stefano Covino
Date    : 19/05/2023
E-mail  : stefano.covino@inaf.it
URL     : http://www.me.oa-brera.inaf.it/utenti/covino


Usage   : to be imported

Remarks :

History : (16/12/2011) First version.
        : (12/01/2012) V. 1.1.0b1.
        : (06/02/2012) V. 1.1.0.
        : (01/04/2012) V. 1.1.1b1.
        : (04/04/2012) V. 1.2.0b1 and new constant.
        : (18/04/2012) V. 1.2.0.
        : (01/08/2012) V. 1.2.1b1.
        : (22/08/2012) V. 1.3.0b1.
        : (29/08/2012) V. 1.3.0.
        : (31/08/2012) V. 1.3.1b1.
        : (22/03/2013) V. 1.3.1.
        : (22/04/2013) New ROS2 pixel size. and V. 1.3.2b1
        : (21/06/2013) New camera code.
        : (01/07/2013) Parameter name check in REM pointing model.
        : (13/08/2013) Better minimization in pointing model computation. V. 1.3.2.
        : (14/08/2013) V. 1.3.3b1. V. 1.3.3b2.
        : (15/08/2013) V. 1.3.3b3.
        : (17/08/2013) V. 1.3.3b4.
        : (21/08/2013) V. 1.4.0b1., 1.4.0b2.
        : (22/08/2013) V. 1.4.0b3.
        : (23/08/2013) V. 1.4.0b4.
        : (24/08/2013) V. 1.4.0 and V. 1.4.1b1.
        : (25/08/2013) V. 1.4.1b2 and 1.5.0b1.
        : (28/08/2013) V. 1.5.0b2.
        : (29/08/2013) V. 1.5.0b3.
        : (04/09/2013) V. 1.5.0b4.
        : (16/09/2013) V. 1.5.0b5.
        : (22/11/2013) V. 1.5.0b6.
        : (04/12/2013) V. 1.5.0b7.
        : (07/01/2014) V. 1.5.08b.
        : (09/01/2014) V. 1.5.0b9.
        : (07/02/2014) V. 1.5.0.
        : (25/07/2014) V. 1.5.1b1.
        : (28/07/2014) V. 1.5.1b2.
        : (05/08/2014) V. 1.5.1b3.
        : (06/08/2014) V. 1.5.1.
        : (20/08/2014) V. 1.5.2b1.
        : (23/07/2015) V. 1.5.2b2.
        : (07/10/2015) V. 1.5.2b3.
        : (10/05/2016) V. 2.0.0.
        : (14/02/2017) V. 2.1.0b1.
        : (16/02/2017) V. 2.1.0b2.
        : (21/02(2017) V. 2.1.0.
        : (04/03/2017) V. 2.1.1.
        : (14/03/2017) V. 2.1.2b1.
        : (28/04/2017) V. 2.1.2.
        : (12/05/2017) V. 2.1.3b1 and 2.1.3b2
        : (16/05/2017) V. 2.1.3.
        : (10/11/2017) V. 2.1.4.
        : (04/06/2019) V. 2.2.0.
        : (07/03/2020) V. 2.2.1.
		: (12/05/2021) V. 2.3.0.
        : (10/03/2022) V. 2.3.1.
        : (19/05/2023) V. 2.3.2.
"""

__version__ = '2.3.2'



__all__ =  ['GetObj', 'GetREMOffsets', 'GetREMSite']



# REM pixel size
REMIRPixSize    = 1.22
ROSSPixSize     = 0.59
ROS2PixSize     = 0.59


# REM center pixels
REMIRXCenter    =   256
REMIRYCenter    =   256
ROSS2XCenter    =   512
ROSS2YCenter    =   512


# Constants
REMIR   =   'REMIR'
ROSS    =   'REM-ROSS'
ROS2    =   'REM-ROS2'
CAMERA  =   'INSTRUME'


# External commands
astro   =   'SRPAstrometry'
astrod  =   'SRPREMAstrometryDeep'
astros  =   'SRPREMAstrometrySearch'


# Observatory location
REMLAT = '-29.2567'
REMLONG = '-70.7292'
REMHEIGHT = 2347.0


# REM headers
RA          =   'RA'
DEC         =   'DEC'
DOBS        =   'DATE-OBS'


