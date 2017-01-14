a=[
    {
        'score': 123,
        'name': 'frank'
    },
    {
        'name': 'jack',
        'score': 44
    },
    {
        'name': 'susan',
        'score': 188
    },
    {
        'name': 'lisa',
        'score': 99
    }
]

b=[
    {
        'score': 12,
        'name': 'frank'
    },
    {
        'name': 'jack',
        'score': 44
    },
    {
        'name': 'susan',
        'score': 223
    },
    {
        'name': 'lisa',
        'score': 99
    }
]

def trend_pk_tool(o, n):
	if o > n:
		return '1'
	elif o == n:
		return '0'
	else:
		return '-1'

def trend_pk(old_list, new_list):
	# You should read both list from redis
	old_list = sorted(old_list, lambda x,y: cmp(x.get("score"), y.get("score")), reverse=True)
	new_list = sorted(new_list, lambda x,y: cmp(x.get("score"), y.get("score")), reverse=True)
	old_uid_list = [i.get('name') for i in old_list]
	new_uid_list = [i.get('name') for i in new_list]
	for i in new_uid_list:
		index = new_uid_list.index(i)
		if i in old_uid_list:
			old_index = old_uid_list.index(i)
			new_list[index].update({'trend': trend_pk_tool(old_index, index)})

		else:
			new_list[index].update({'trend':'1'})
		new_list[index].update({'rank':str(index)})
	return new_list


def map_uid_to_score_info(score_list):
	redis_cache = {}
	for i in score_list:
		uid = i.get('name')
		redis_cache.update({
			uid:{
					'score':i.get('score'),
					'trend':i.get('trend'),
					'rank':i.get('rank')
				}
			})

	return redis_cache


if __name__ == '__main__':
	ret = trend_pk(a, b)
	redis_cache = map_uid_to_score_info(ret)
	print redis_cache
