import math, random
#
# def coordinates(branches,radius,center_lat,center_lon, k):
#     angle = math.pi*2*k/branches
#     dx = radius*math.cos(angle)
#     dy = radius*math.sin(angle)
#     lat = center_lat + (180/math.pi)*(dy/6378137)
#     lon = center_lon + (180/math.pi)*(dx/6378137)/math.cos(center_lat*math.pi/180)
#     print(lat, lon)
#
# for k in range (1,30):
#     coordinates(1,random.randint(1000,50000),12.972442,77.580643, k)


# # inputs
# radius = 50.0 # m - the following code is an approximation that stays reasonably accurate for distances < 100km
# centerLat = 12.972442 # latitude of circle center, decimal degrees
# centerLon = 77.580643 # Longitude of circle center, decimal degrees
#
# # parameters
# N = 10 # number of discrete sample points to be generated along the circle
#
# # generate points
# # circlePoints = []
# for k in range(N):
#     # compute
#     angle = math.pi*2*k/N
#     dx = radius*math.cos(angle)
#     dy = radius*math.sin(angle)
#     # point = {}
#     lat=centerLat + (180/math.pi)*(dy/6378137)
#     print(type(lat))
#     lon=centerLon + (180/math.pi)*(dx/6378137)/math.cos(centerLat*math.pi/180)
#     # add to list
#     # circlePoints.append(point)
#     print([lat,lon])

# print (circlePoints)

#
# t = {'merchant': ['9226'], 'zone': ['east'], 'state': ['Kolkata'], 'city': ['Kolkata'], 'Address': ['Kolkata'], 'PIN': [634636], 'lat': ['22.57264500'], 'lng': ['88.36399901'], 'shop-number': [634636]}
#
# print(t['merchant'][0])



{"name":"test","startTime":"2019-04-05 00:00:00","endTime":"2019-04-30 23:59:59","lineItems":[{"coupons":[194,196],"segment":{"op":"and","segments":["403","384",{"op":"not","segments":["265"]}]}},{"coupons":[194,196],"segment":{"op":"and","segments":["265",{"op":"not","segments":["283"]}]}}],"userGroup":42}
