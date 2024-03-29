string = '''
"activityBar.background": "#011627",
"activityBar.border": "#219fd544",
"activityBar.foreground": "#99d0f7",
"activityBarBadge.background": "#219fd5",
"activityBarBadge.foreground": "#ffffff",
"badge.background": "#219fd5",
"badge.foreground": "#ffffff",
"button.background": "#03648a",
"button.foreground": "#ffffff",
"button.hoverBackground": "#219fd5",
"contrastActiveBorder": "#122d42",
"contrastBorder": "#122d42",
"debugExceptionWidget.background": "#011627",
"debugToolBar.background": "#022846",
"diffEditor.insertedTextBackground": "#99b76d23",
"diffEditor.insertedTextBorder": "#addb6733",
"diffEditor.removedTextBackground": "#ef535033",
"diffEditor.removedTextBorder": "#ef53504d",
"editor.background": "#011627",
"editor.findMatchHighlightBackground": "#103362",
"editor.foreground": "#a7dbf7",
"editor.hoverHighlightBackground": "#0c4994",
"editor.inactiveSelectionBackground": "#7e57c25a",
"editor.lineHighlightBackground": "#0c499477",
"editor.rangeHighlightBackground": "#103362",
"editor.selectionBackground": "#103362",
"editor.selectionHighlightBackground": "#103362",
"editor.wordHighlightBackground": "#103362",
"editor.wordHighlightStrongBackground": "#103362",
"editorBracketMatch.background": "#219fd54d",
"editorCursor.foreground": "#219fd5",
"editorError.foreground": "#ef5350",
"editorGroup.border": "#219fd544",
"editorGroupHeader.tabsBackground": "#011627",
"editorGutter.background": "#011627",
"editorHoverWidget.background": "#011627",
"editorHoverWidget.border": "#5f7e97",
"editorIndentGuide.activeBackground": "#c792ea",
"editorIndentGuide.background": "#0e2c45",
"editorLineNumber.foreground": "#219fd5",
"editorOverviewRuler.commonContentForeground": "#7e57c2",
"editorOverviewRuler.currentContentForeground": "#7e57c2",
"editorOverviewRuler.incomingContentForeground": "#7e57c2",
"editorSuggestWidget.background": "#2c3043",
"editorSuggestWidget.border": "#2b2f40",
"editorSuggestWidget.foreground": "#d6deeb",
"editorSuggestWidget.highlightForeground": "#ffffff",
"editorSuggestWidget.selectedBackground": "#5f7e97",
"editorWarning.foreground": "#ffca28",
"editorWhitespace.foreground": "#3b3a32",
"editorWidget.background": "#0b2942",
"editorWidget.border": "#262a39",
"errorForeground": "#ef5350",
"foreground": "#d6deeb",
"gitDecoration.modifiedResourceForeground": "#219fd5",
"gitDecoration.untrackedResourceForeground": "#5abeb0",
"input.background": "#0b253a",
"input.border": "#5f7e97",
"input.foreground": "#ffffffcc",
"input.placeholderForeground": "#5f7e97",
"inputOption.activeBorder": "#ffffff",
"inputValidation.errorBackground": "#ef5350",
"inputValidation.errorBorder": "#ef5350",
"inputValidation.infoBackground": "#219fd5",
"inputValidation.infoBorder": "#219fd5",
"inputValidation.warningBackground": "#f7ecb5",
"inputValidation.warningBorder": "#f7ecb5",
"inputValidation.warningForeground": "#000000",
"list.activeSelectionBackground": "#219fd5",
"list.dropBackground": "#011627",
"list.focusBackground": "#03648a",
"list.focusForeground": "#ffffff",
"list.highlightForeground": "#ffffff",
"list.hoverBackground": "#011627",
"list.hoverForeground": "#219fd5",
"list.inactiveSelectionBackground": "#0e293f",
"list.inactiveSelectionForeground": "#5f7e97",
"list.invalidItemForeground": "#975f94",
"notificationLink.foreground": "#80cbc4",
"notificationToast.border": "#219fd544",
"notifications.background": "#011627",
"notifications.foreground": "#ffffffcc",
"panel.background": "#011627",
"panel.border": "#219fd5",
"panelTitle.activeBorder": "#5f7e97",
"panelTitle.activeForeground": "#219fd5",
"panelTitle.inactiveForeground": "#5f7e97",
"peekView.border": "#f7ecb5",
"peekViewEditor.background": "#011627",
"peekViewEditor.matchHighlightBackground": "#7e57c25a",
"peekViewResult.background": "#011627",
"peekViewResult.matchHighlightBackground": "#7e57c25a",
"peekViewResult.selectionBackground": "#2e3250",
"peekViewResult.selectionForeground": "#cecece",
"peekViewTitle.background": "#011627",
"peekViewTitleDescription.foreground": "#697098",
"peekViewTitleLabel.foreground": "#cecece",
"pickerGroup.border": "#219fd544",
"quickInput.list.focusBackground": "#219fd5",
"scrollbar.shadow": "#010b14",
"scrollbarSlider.activeBackground": "#084d8180",
"scrollbarSlider.background": "#084d8180",
"scrollbarSlider.hoverBackground": "#084d8180",
"selection.background": "#4373c2",
"sideBar.background": "#011627",
"sideBar.border": "#219fd544",
"sideBar.foreground": "#7799bb",
"sideBarSectionHeader.background": "#011627",
"sideBarSectionHeader.foreground": "#7799bb",
"sideBarTitle.foreground": "#7799bb",
"statusBar.background": "#219fd5",
"statusBar.debuggingBackground": "#b15a91",
"statusBar.noFolderBackground": "#011627",
"statusBarItem.activeBackground": "#03648a",
"statusBarItem.hoverBackground": "#03648a",
"statusBarItem.prominentBackground": "#03648a",
"statusBarItem.prominentHoverBackground": "#03648a",
"tab.activeBackground": "#0b2942",
"tab.activeBorderTop": "#219fd5",
"tab.activeForeground": "#d2dee7",
"tab.inactiveBackground": "#010e1a",
"tab.inactiveForeground": "#5f7e97",
"terminal.ansiBlack": "#011627",
"textLink.activeForeground": "#98c8ed",
"textLink.foreground": "#219fd5",
"titleBar.activeBackground": "#112233",
"titleBar.activeForeground": "#eeefff",
"titleBar.border": "#303030",
"titleBar.inactiveBackground": "#000a11",
"walkThrough.embeddedEditorBackground": "#001111",
"widget.shadow": "#219fd5",'''

hexcodes = []

codes = string.split('\n')[1:]

for number in codes:
    number = number.split(':')[1]
    number = "".join(filter(lambda x: x in ['#','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'],number))
    hexcodes.append(number)

output = []
for code in hexcodes:
    if code not in output:
        output.append(code)

print(output)