# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Eficent (<http://www.eficent.com/>)
#              <contactr@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    "name": "Project Meeting Integration",
    "version": "1.0",
    "author": "Eficent",
    "website": "www.eficent.com",
    "category": "Generic Modules/Projects & Services",
    "depends": ["project","crm"],
    "description": """
    
     == Manage the meetings related to your projects ==
    
    Eficent brings you this module to better manage the meetings related to your projects.
    
    The 'Meetings' tab in the project  form, and a link to meetings view helps you to create new meetings from the project, and 
        to better track the status of existing meetings.
          
         
    """,
    "init_xml": [
                ],
    "update_xml": [
        "security/ir.model.access.csv",
        "security/project_communications_meetings_security.xml",
        "project_communications_meetings_view.xml",     
        "project_view.xml",   

    ],
    'demo_xml': [

    ],
    'test':[
    ],
    #SIN ADAPTAR
    'installable': True,
    'active': False,
    'certificate': '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
