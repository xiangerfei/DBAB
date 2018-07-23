# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
import models



#class HostAdmin(admin.ModelAdmin):
#	list_display = ('HostIP','DBComment','DBMaster1','DBSlave1',)


#admin.site.register(models.HostInfo, HostAdmin)



@admin.register(models.HostInfo)
class UserAdmin(admin.ModelAdmin):
	list_display = ('HostIP','VirtualIp1', 'DBMaster1','DBSlave1','MashineModel','MemerySize','ImportLevel','xxxxx','DBComment','Company')
	list_display_links = ('HostIP', 'DBMaster1',)
#	list_per_page=2  #分页查询
#	list_max_show_all = 100 #真实数据<该值时，才会有显示全部
#	paginator = Paginator	# 分页插件


#	list_editable = ('DBComment',)	# 可点击编辑,不可与链接list_display_links同时存在。
	def xxxxx(self, obj):
		return "占位"


#	class Ugg(admin.SimpleListFilter):
#		title = ('重要级别')
#		parameter_name = 'xxxxxx'
#	
#		def lookups(self, request, model_admin):
#			"""
#			显示筛选选项
#			:param request: 
#			:param model_admin: 
#			:return: 
#			"""
#			return models.HostInfo.objects.values_list('HostIP', 'ImportLevel')
#		
#		def queryset(self, request, queryset):
#			"""
#			点击查询时，进行筛选
#			:param request: 
#			:param queryset: 
#			:return: 
#			"""
#			v = self.value()
#			return queryset.filter(HostIP=v)
#	list_filter = ('HostIP',Ugg,)
	

	search_fields = ('HostIP','DBMaster1')  # 提供搜索得字段




	

#	date_hierarchy = 'CraeteTime'	 #这个针对博客系统按时间分类。很好。


#	perverve_filters = False   # 对条目操作过后，是否保留过滤条件。


#	save_as = False # 
#	save_as_continue = True，点击保存并继续编辑

# 如果 save_as=True，save_as_continue = True， 点击Sava as new 按钮后继续编辑。
# 如果 save_as=True，save_as_continue = False，点击Sava as new 按钮后返回列表。
#New in Django 1.10.


	save_on_top = False #详细页面，在页面上方是否也显示保存删除等按钮

	def func(self, request, queryset):
		print(self, request, queryset)
		print(request.POST.getlist('_selected_action'))

	func.short_description = "自定义Actions"
	actions = [func,]

	actions_on_top = True

	actions_on_bottom = False

	actions_selectoin_counter = True

#-------------------------定制HTML模板---------------------------#
#	add_form_template = None
#	change_form_template = None
#	change_list_template = None
#	delete_confirmation_template = None
#	delete_selected_confirmation_template = None
#	object_history_template = None



#---------------- fields 详细页面时，显示字段的字段------------#
#	fields = ('HostIP','DBMaster1',); # 默认全部显示
#---------------- exclude 详细页面时， 排除的字段 -------------#
#	exclude = ('HostUser','HostPass','DBUser','DBPass') #增加的form里面也没有了。。
#---------------- 详细页面时，只读字段 ------------------------#
#	readonly_fields = ('HostIP','HostUser',) 

#---------------- fieldsets 详细页面时，使用fieldsets标签对数据进行分割显示----
	
	fieldsets = (
	('基本数据', {
		'fields': ('HostIP','ManagerIp','VirtualIp1','VirtualIp2', 'DBMaster1','DBSlave1','DBSlave2','ImportLevel',)
	}),
	('账号信息', {
#		'classes': ('collapse', 'wide', 'extrapretty'),	# 样式
		'classes': ('collapse', ),	# 样式
		'fields': ('HostUser', 'HostPass','DBUser','DBPass','DBSlave3','DBSlave4',),
	}),
	('硬件信息',{
		'classes':('collapse',),
		'fields':('MashineModel','MemerySize'),
	}),
	('其他信息',{
		'fields': ('DBComment','Company','CraeteTime','UpdateTime'),
	}),
	
	)

#--------------------- 详细页面时，M2M显示时。数据移动选择（方向：上下和左右）
#	filter_vertical = ('m2m字段',) # 或者filter_horizontal = ("m2m字段",)



#-------------------- 列表时，数据排序规则 ----------------
# 	ordering = ('HostIP',)


#-------------------- view_on_site 编辑时，是否在页面上显示view on set
#	view_on_site = False
#	def view_on_site(self, obj):
#		return "https://www.baidu.com"


#	empty_value_display = "列数据为空时，显示默认值"
	prepopulated_fields = {"DBComment": ("HostIP","HostUser",)}	# 使用JS关联输入

