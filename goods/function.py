from utils.common import *
from users.models import RecordBrowse
from carts.models import *
# 更新用户浏览记录
def update_user_browe_record(request):
    # 最大记录条数
    max_limit = 5
    # 用户是否登录
    if not is_login(request):
        return

    # 如果用户登录
    good_id = get_getvalue(request, 'id')
    user_id = get_session(request, 'uid')

    #1. 如果商品存在,则只要更新商品的浏览记录的update_time
    try:
        record = RecordBrowse.objects.get(browse_good_id=good_id, browse_user_id=user_id)
        record.save()
    # 2. 如果商品不存在
    except RecordBrowse.DoesNotExist:
        records = RecordBrowse.objects.filter(browse_user_id=user_id).order_by('update_time')
        # 判断用户浏览记录是否达到5条,没有达到,直接插入
        if records.count() < max_limit:
            rb = RecordBrowse()
            rb.browse_good_id = good_id
            rb.browse_user_id = user_id
            rb.save()
        else:
            rb = records[0]
            rb.browse_good_id = good_id
            rb.save()


        # 如果用户记录是5条,则更新最早的那条记录id


# 获得商品总数
def get_total_cart_sum(view_func):

    def wrapper(request, *args, **kwargs):
        total = 0
        carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))
        for good in carts:
            total += good.cart_amount

        request.total = total

        return view_func(request, *args, **kwargs)

    return wrapper
