from django.contrib import admin
from .models import EbTerminal
# Register your models here.




class TerminalAdmin(admin.ModelAdmin):
	#fields = ['pub_date','question_text']
	fieldsets = [(None,{'fields':['name']}),('Date information',{'fields':['reg_time'],'classes':['collapse']})]
	list_display = ('name','terminal_name','status','terminal_type','addr')
	list_filter = ['terminal_type']
	search_fields = ['terminal_name','name']

admin.site.register(EbTerminal,TerminalAdmin)