#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2016 sorax
#
#  This file is part of the detektor.fm kodi plugin.
#
#  This plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this plugin.  If not, see <http://www.gnu.org/licenses/>.


import os
import sys
import urllib
import urlparse

import xbmcaddon
import xbmcgui
import xbmcplugin


addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addonpath = addon.getAddonInfo('path')


#base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
#args = urlparse.parse_qs(sys.argv[2][1:])


def main():
	li_stream1 = xbmcgui.ListItem(label=addon.getLocalizedString(30011), thumbnailImage=addonpath + "/resources/media/wort.png")
	li_stream2 = xbmcgui.ListItem(label=addon.getLocalizedString(30012), thumbnailImage=addonpath + "/resources/media/musik.png")

	xbmcplugin.addDirectoryItem(handle=addon_handle, url='http://detektor.fm/stream/mp3/wort/', listitem=li_stream1, isFolder=False)
	xbmcplugin.addDirectoryItem(handle=addon_handle, url='http://detektor.fm/stream/mp3/musik/', listitem=li_stream2, isFolder=False)

	xbmcplugin.endOfDirectory(addon_handle)


if __name__ == '__main__':
	main()
