from urllib import request, error


def issue_list(start):
    start = start * 50
    host = 'https://bugly.qq.com'
    page = '/v2/issueList?'

    params = 'start=' + str(start) \
             + '&searchType=errorType' + \
             '&exceptionTypeList=Crash,Native' + \
             '&pid=1' + \
             '&platformId=1' + \
             '&sortOrder=desc' + \
             '&rows=50' + \
             '&sortField=crashCount' + \
             '&appId=d98a6960d7' + \
             '&fsn=003c87eb-8c7e-48b7-9901-6d1779c6dfcc'

    url = host + page + params

    headers = {
        'X-token': '814585267',
        'Accept': 'application/json;charset=utf-8',
        'x-csrf-token': 'Ab5m4ZeWsaOxNLuSVfT3OXdB',
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Content-Type': 'application/json;charset=utf-8',
        'Referer': 'https://bugly.qq.com/v2/crash-reporting/crashes/d98a6960d7?pid=1&sortField=crashCount&sortOrder=desc&start=0',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'btcu_id=ed70f24fdc9235e8bc045c4c55a836755aea9eb6b0dc6; pgv_pvi=1553976320; RK=kbSoz2plS0; ptcz=79a4069068d1673ba15d973f7e7aca9455f95abbde9b44625167c8361d34bbc6; pgv_pvid=1021383505; tvfe_boss_uuid=a9fb74b55ead28c8; o_cookie=451477973; _ga=GA1.2.877053183.1526950312; vc=vc-e5e3e667-5be2-4463-8c1d-2bc4dc3133d7; btcu_id=fbe3a52d-887e-4f0b-87eb-8248ec69fbe2; pac_uid=1_451477973; ptui_loginuin=451477973; pt2gguin=o0451477973; luin=o0451477973; lskey=000100006ccfc114d1c01a0a84922fe0c2be44e9a1fe3ac4e267cd91169aaa4da2eec75cb58f0c898619634d; _gid=GA1.2.1733470217.1542185609; token-skey=8fff1338-e3d7-e9b0-f780-12b5619779e3; token-lifeTime=1542349590; pgv_si=s4446401536; _qpsvr_localtk=0.8575546452372875; ptisp=cm; uin=o0451477973; skey=@XgnZEz8wT; NODINX_SESS=oXphL4SG33RFOFs0wn11E7ca2x44k2F3mZqGr2VVeAS2Z51fVNexYfzmboXxYu5g; csrfToken=Ab5m4ZeWsaOxNLuSVfT3OXdB; _gat=1; bugly_session=eyJpdiI6Ikxzd0RjZlE2NDNiSkhmWWtySTBJOWc9PSIsInZhbHVlIjoiaEswTWJcL0JLMFo5QUkxNndMUGw4V08yM0VJQllxK3pscDBrN0s5T3lrcFBkVGNxTEQ1eUQ4clZxb25jT2ZHQ0pGZno0MjJmY3R4N3VtelFPWnlsTDBnPT0iLCJtYWMiOiIwZTYzZTllMTgwYzFhMzk2OGEwOTk2Zjk1ZTA2YjdhY2I5ZjUzYzJlOTg2N2QzZmU4MTU1ZTI5ZjI4YWFiMWFiIn0%3D; referrer=eyJpdiI6ImllTVVpRTEzZWdLd2Y4U2pnTEV3N0E9PSIsInZhbHVlIjoidVZCVG5oK2FZSG1uenYxWDR5VldzTHZJcERrcG9mNFlnek1Rbmh3Vkc3YkhwQjZkSzdTa1BuT0FicUc3alFSSzV4VzA0K1FXUGY3cjNidHlkUFIxRlwvQm1qeGc5c2dWS1FnQ0NPcnV3K2dkbTNzMWVnenVLaVhZUitjM0NLSkdKVVdFd2RiM1lyS3NPWkpWaGhNMHlIU0ZZSHdMZG5LcFNUUTh6VkdEVklUVT0iLCJtYWMiOiI2ZDYzNzAxYmM1MWU2NmJjZmY1YzM3MjQxY2M4ZmVmMWQ3ZmM5YzAyY2VlZDNmYTliYzA4NjdlZmM1YTdkMDFiIn0%3D; vc=vc-6a81432d-d4be-4bca-a23c-9a286c2cc0b3; vc.sig=RzhW6CaM14JQr8MzkayGZMUlgwg1CaBD56cUWNdJV1s',
    }

    req = request.Request(url, None, headers, 'GET')

    try:
        response = request.urlopen(req)
        result = response.read().decode('utf-8')

        print(result)
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, '\n')
    except error.URLError as e:
        print(e.reason)


if __name__ == '__main__':
    issue_list(0)