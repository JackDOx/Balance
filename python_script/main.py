import re
def balance(*args, **kargs):

        result = Element('output')

        # tách chất / Get Chemical substances
        def getChem(chem):
            firstEChem = []
            x = re.findall("[A-Z][a-z]?[1-9]?[1-9]?", chem)
            x.sort()
            for f in range(len(x)):
                s = re.findall("[A-Z][a-z]?", x[f])
                s = str(s[0])
              
                firstEChem.append(s)
                
            return firstEChem

        # funtion() tách hệ số/ Get chemical value//
        def getValue(chem):
            firstEValue = []
            x = re.findall("[A-Z][a-z]?[1-9]?[1-9]?", chem)
            x.sort()
            for f in range(len(x)):
                h = re.findall("[0-9][0-9]?", x[f])
                try:
                    h = int(h[0])
                except:
                    h = 1

                firstEValue.append(h)
            return firstEValue




        #test a value convertable to int
        def into(dun):
            try:
                dun = int(dun)
                return True
            except:
                return False

        # 1stE
        firstE = f"{Element('first').value}"
        op = []
        op.extend(firstE)
        op.append(None)
        op.insert(0, None)
        fec = getChem(firstE)
        fev = getValue(firstE)

        # 2ndE
        secondE = f"{Element('second').value}"
        sec = getChem(secondE)
        sev = getValue(secondE)


        # 3rdE
        thirdE = f"{Element('third').value}"
        thc = getChem(thirdE)
        thv = getValue(thirdE)

        # 4thE

        fourthE = f"{Element('fourth').value}"
        foc = getChem(fourthE)
        fov = getValue(fourthE)

        try:
            if fourthE == "":
                for a in range(1,32):
                    for b in range(1,32):
                        for c in range(1, 32):
                            e = []
                            f = []
                            g = []
                            h = []
                            for x in range(len(fec)):
                                try:
                                    i = sec.index(fec[x]) # search position of Na in second E
                                    o = sev[i]
                                    mo = a*fev[x] + b*sev[i]
                                    e.append(mo)
                                    
                                except: # ramaining first E
                                    mi = a*fev[x]
                                    e.append(mi)

                                ma = thc.index(fec[x])
                                mo = c*thv[ma]
                                g.append(mo)

                            for x in range(len(sec)):
                                if sec[x] not in fec:
                                    mp = b*sev[x]
                                    f.append(mp)
                                    mc = thc.index(sec[x])
                                    md = c*thv[mc]
                                    g.append(md)
                            if e+f == g:
                                fe = a
                                se = b
                                te = c

                                break
                        if e+f == g:
                            fe = a
                            se = b
                            te = c

                            break
                    if e+f == g:
                        fe = a
                        se = b
                        te = c

                        break

            
            else:
                for a in range(1, 17):
                    for b in range(1, 50):
                        for c in range(1, 50):
                            for d in range(1, 22):
                                e = []
                                f = []
                                g = []
                                h = []
                                for x in range(len(fec)):
                                    try:
                                        i = sec.index(fec[x]) # search position of Na in second E
                                        o = sev[i]
                                        mo = a*fev[x] + b*sev[i]
                                        e.append(mo)

                                    except: # ramaining first E
                                        mi = a*fev[x]
                                        e.append(mi)
                                    #third E    
                                    try:
                                        u = thc.index(fec[x])
                                        try:
                                            j = foc.index(fec[x])
                                            iu = c*thv[u]+ d*fov[j]
                                            g.append(iu)
                                        except:     
                                            g.append(c*thv[u])

                                    except:
                                        hm = foc.index(fec[x])
                                        p = d*fov[hm]
                                        g.append(p)

                                # Remaining second E and search them in third E and fourth E
                                for x in range(len(sec)):
                                    if sec[x] not in fec:
                                        mp = b*sev[x]
                                        f.append(mp)
                                        try:
                                            l = thc.index(sec[x])
                                            try:
                                                mv = foc.index(sec[x])
                                                mj = c*thv[l] + d*fov[mv]
                                                h.append(mj)

                                            except:
                                                h.append(c*thv[l])

                                        except:
                                            lm = foc.index(sec[x])
                                            h.append(d*fov[lm])
                                if e == g and f == h:
                                    fe = a
                                    se = b
                                    te = c
                                    foe = d
                                    break
                            if e == g and f == h:
                                fe = a
                                se = b
                                te = c
                                foe = d
                                break
                        if e == g and f == h:
                            fe = a
                            se = b
                            te = c
                            foe = d
                            break
                    if e == g and f == h:
                        fe = a
                        se = b
                        te = c
                        foe = d
                        break

            if fourthE == "":
                if fe >30 and se > 30  and te > 30:
                    result.write("Error no result")
                else:
                    partial_result = (fe, se, te)
                    main_result =f"{str(fe)}{firstE}   +   {str(se)}{secondE}    ->   {str(te)}{thirdE}"
                    result.write(main_result)
            else:
                if fe >15 and se > 48 and te> 48:
                    result.write("Error no result")
                else:
                    partial_result = (fe, se, te, foe)
                    main_result =f"{str(fe)}{firstE}   +   {str(se)}{secondE}    ->   {str(te)}{thirdE}   +   {str(foe)}{fourthE}"
                    result.write(main_result)
        except:
            result.write("Error! heck your chemical substances again")