
def splitline(pt1, pt2, percent=0.5):
    '''
    Return a point which splits the given line at the
    given percentag...

    Example: splitline( (0,0), (20, 30), 0.1)
    '''

    pt1_x, pt1_y = pt1
    pt2_x, pt2_y = pt2

    deltax = (pt2_x - pt1_x) * percent
    deltay = (pt2_y - pt1_y) * percent

    return pt1_x + deltax, pt1_y + deltay

def calculate_bezier(points, steps = 30):
    '''
    Arbitrary depth and arbitrary precision bezier implementation.  Takes
    a list of (x,y) point tuples and returnes the points to draw for the
    bezier curve.
    '''
    ret = []
    points = [ (float(x),float(y)) for x,y in points ]

    for i in xrange(steps+1):

        pcent = i / float(steps)

        layers = [ points, ]
        while len(layers[-1]) != 1:
            l_points = layers[-1]
            newpoints = [ splitline( l_points[i], l_points[i+1], pcent) for i in xrange(len(l_points)-1) ]
            layers.append(newpoints)

        ret.append(layers[-1][0])

    return ret

if __name__ == '__main__':
    print calculate_bezier( [ (0,0), (3, 20), (20, 23), (20, 20)] )

    print calculate_bezier( [ (0,0), (10,10) ], 10)

