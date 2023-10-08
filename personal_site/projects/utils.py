from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate(request, objects_data, objects_count):

    page = request.GET.get('page')
    paginator = Paginator(object_list=objects_data, per_page=objects_count)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        data = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        data = paginator.page(page)

    left_index = int(page) - 2
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 3
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, data
