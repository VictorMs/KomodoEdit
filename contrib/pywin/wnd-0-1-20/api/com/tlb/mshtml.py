
"""
...just an excerp from mshtml_gen

"""


from ctypes import *
from ctypes.com import IUnknown, GUID, STDMETHOD, HRESULT
from ctypes.com.automation import IDispatch, BSTR, VARIANT, dispinterface, \
                                  DISPMETHOD, DISPPARAMS, EXCEPINFO
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SAFEARRAYBOUND(Structure):
	_fields_ = [("cElements", c_ulong),
						("lLbound", c_long)]

class SAFEARRAY(Structure):
	_fields_= [("cDims", c_ushort),
	("fFeatures", c_ushort),
	("cbElements", c_ulong),
	("cLocks", c_ulong),
	("pvData", c_void_p),
	("rgsabound", SAFEARRAYBOUND*1)]


class IOmHistory(IDispatch):
	pass

class IOmNavigator(IDispatch):
	pass

class IHTMLImageElementFactory(IDispatch):
   pass

class IHTMLEventObj(IDispatch):
   pass

class IHTMLScreen(IDispatch):
   pass

class IHTMLOptionElementFactory(IDispatch):
   pass

class IHTMLStyleSheetsCollection(IDispatch):
   pass

class IHTMLStyleSheet(IDispatch):
   pass


class IHTMLWindow2(IDispatch):
    _iid_ = GUID('{332C4427-26CB-11D0-B483-00C04FD90119}')

class IHTMLLocation(IDispatch):
    _iid_ = GUID('{163BB1E0-6E00-11CF-837A-48DC04C10000}')

class IHTMLFramesCollection2(IDispatch):
    _iid_ = GUID('{332C4426-26CB-11D0-B483-00C04FD90119}')


class IHTMLSelectionObject(IDispatch):
    _iid_ = GUID('{3050F25A-98B5-11CF-BB82-00AA00BDCE0B}')

class IHTMLFiltersCollection(IDispatch):
    _iid_ = GUID('{3050F3EE-98B5-11CF-BB82-00AA00BDCE0B}')


class IHTMLStyle(IDispatch):
    _iid_ = GUID('{3050F25E-98B5-11CF-BB82-00AA00BDCE0B}')

class IHTMLElement(IDispatch):
    _iid_ = GUID('{3050F1FF-98B5-11CF-BB82-00AA00BDCE0B}')

class IHTMLDocument2(IDispatch):
    _iid_ = GUID('{332C4425-26CB-11D0-B483-00C04FD90119}')

class IHTMLElementCollection(IDispatch):
    _iid_ = GUID('{3050F21F-98B5-11CF-BB82-00AA00BDCE0B}')




IHTMLWindow2._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "item", POINTER(VARIANT), POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_length", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_frames", POINTER(POINTER(IHTMLFramesCollection2))),
    STDMETHOD(HRESULT, "_put_defaultStatus", BSTR),
    STDMETHOD(HRESULT, "_get_defaultStatus", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_status", BSTR),
    STDMETHOD(HRESULT, "_get_status", POINTER(BSTR)),
    STDMETHOD(HRESULT, "setTimeout", BSTR, c_long, POINTER(VARIANT), POINTER(c_long)),
    STDMETHOD(HRESULT, "clearTimeout", c_long),
    STDMETHOD(HRESULT, "alert", BSTR),
    STDMETHOD(HRESULT, "confirm", BSTR, POINTER(c_int)),
    STDMETHOD(HRESULT, "prompt", BSTR, BSTR, POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_Image", POINTER(POINTER(IHTMLImageElementFactory))),
    STDMETHOD(HRESULT, "_get_location", POINTER(POINTER(IHTMLLocation))),
    STDMETHOD(HRESULT, "_get_history", POINTER(POINTER(IOmHistory))),
    STDMETHOD(HRESULT, "close"),
    STDMETHOD(HRESULT, "_put_opener", VARIANT),
    STDMETHOD(HRESULT, "_get_opener", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_navigator", POINTER(POINTER(IOmNavigator))),
    STDMETHOD(HRESULT, "_put_name", BSTR),
    STDMETHOD(HRESULT, "_get_name", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_parent", POINTER(POINTER(IHTMLWindow2))),
    STDMETHOD(HRESULT, "open", BSTR, BSTR, BSTR, c_int, POINTER(POINTER(IHTMLWindow2))),
    STDMETHOD(HRESULT, "_get_self", POINTER(POINTER(IHTMLWindow2))),
    STDMETHOD(HRESULT, "_get_top", POINTER(POINTER(IHTMLWindow2))),
    STDMETHOD(HRESULT, "_get_window", POINTER(POINTER(IHTMLWindow2))),
    STDMETHOD(HRESULT, "navigate", BSTR),
    STDMETHOD(HRESULT, "_put_onfocus", VARIANT),
    STDMETHOD(HRESULT, "_get_onfocus", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onblur", VARIANT),
    STDMETHOD(HRESULT, "_get_onblur", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onload", VARIANT),
    STDMETHOD(HRESULT, "_get_onload", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onbeforeunload", VARIANT),
    STDMETHOD(HRESULT, "_get_onbeforeunload", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onunload", VARIANT),
    STDMETHOD(HRESULT, "_get_onunload", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onhelp", VARIANT),
    STDMETHOD(HRESULT, "_get_onhelp", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onerror", VARIANT),
    STDMETHOD(HRESULT, "_get_onerror", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onresize", VARIANT),
    STDMETHOD(HRESULT, "_get_onresize", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onscroll", VARIANT),
    STDMETHOD(HRESULT, "_get_onscroll", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_document", POINTER(POINTER(IHTMLDocument2))),
    STDMETHOD(HRESULT, "_get_event", POINTER(POINTER(IHTMLEventObj))),
    STDMETHOD(HRESULT, "_get__newEnum", POINTER(POINTER(IUnknown))),
    STDMETHOD(HRESULT, "showModalDialog", BSTR, POINTER(VARIANT), POINTER(VARIANT), POINTER(VARIANT)),
    STDMETHOD(HRESULT, "showHelp", BSTR, VARIANT, BSTR),
    STDMETHOD(HRESULT, "_get_screen", POINTER(POINTER(IHTMLScreen))),
    STDMETHOD(HRESULT, "_get_Option", POINTER(POINTER(IHTMLOptionElementFactory))),
    STDMETHOD(HRESULT, "focus"),
    STDMETHOD(HRESULT, "_get_closed", POINTER(c_int)),
    STDMETHOD(HRESULT, "blur"),
    STDMETHOD(HRESULT, "scroll", c_long, c_long),
    STDMETHOD(HRESULT, "_get_clientInformation", POINTER(POINTER(IOmNavigator))),
    STDMETHOD(HRESULT, "setInterval", BSTR, c_long, POINTER(VARIANT), POINTER(c_long)),
    STDMETHOD(HRESULT, "clearInterval", c_long),
    STDMETHOD(HRESULT, "_put_offscreenBuffering", VARIANT),
    STDMETHOD(HRESULT, "_get_offscreenBuffering", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "execScript", BSTR, BSTR, POINTER(VARIANT)),
    STDMETHOD(HRESULT, "toString", POINTER(BSTR)),
    STDMETHOD(HRESULT, "scrollBy", c_long, c_long),
    STDMETHOD(HRESULT, "scrollTo", c_long, c_long),
    STDMETHOD(HRESULT, "moveTo", c_long, c_long),
    STDMETHOD(HRESULT, "moveBy", c_long, c_long),
    STDMETHOD(HRESULT, "resizeTo", c_long, c_long),
    STDMETHOD(HRESULT, "resizeBy", c_long, c_long),
    STDMETHOD(HRESULT, "_get_external", POINTER(POINTER(IDispatch))),
]


IHTMLLocation._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "_put_href", BSTR),
    STDMETHOD(HRESULT, "_get_href", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_protocol", BSTR),
    STDMETHOD(HRESULT, "_get_protocol", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_host", BSTR),
    STDMETHOD(HRESULT, "_get_host", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_hostname", BSTR),
    STDMETHOD(HRESULT, "_get_hostname", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_port", BSTR),
    STDMETHOD(HRESULT, "_get_port", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_pathname", BSTR),
    STDMETHOD(HRESULT, "_get_pathname", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_search", BSTR),
    STDMETHOD(HRESULT, "_get_search", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_hash", BSTR),
    STDMETHOD(HRESULT, "_get_hash", POINTER(BSTR)),
    STDMETHOD(HRESULT, "reload", c_int),
    STDMETHOD(HRESULT, "replace", BSTR),
    STDMETHOD(HRESULT, "assign", BSTR),
    STDMETHOD(HRESULT, "toString", POINTER(BSTR)),
]

IHTMLFramesCollection2._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "item", POINTER(VARIANT), POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_length", POINTER(c_long)),
]


IHTMLSelectionObject._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "createRange", POINTER(POINTER(IDispatch))),
    STDMETHOD(HRESULT, "empty"),
    STDMETHOD(HRESULT, "clear"),
    STDMETHOD(HRESULT, "_get_type", POINTER(BSTR)),
]

IHTMLFiltersCollection._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "_get_length", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get__newEnum", POINTER(POINTER(IUnknown))),
    STDMETHOD(HRESULT, "item", POINTER(VARIANT), POINTER(VARIANT)),
]

IHTMLStyle._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "_put_fontFamily", BSTR),
    STDMETHOD(HRESULT, "_get_fontFamily", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_fontStyle", BSTR),
    STDMETHOD(HRESULT, "_get_fontStyle", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_fontVariant", BSTR),
    STDMETHOD(HRESULT, "_get_fontVariant", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_fontWeight", BSTR),
    STDMETHOD(HRESULT, "_get_fontWeight", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_fontSize", VARIANT),
    STDMETHOD(HRESULT, "_get_fontSize", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_font", BSTR),
    STDMETHOD(HRESULT, "_get_font", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_color", VARIANT),
    STDMETHOD(HRESULT, "_get_color", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_background", BSTR),
    STDMETHOD(HRESULT, "_get_background", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_backgroundColor", VARIANT),
    STDMETHOD(HRESULT, "_get_backgroundColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_backgroundImage", BSTR),
    STDMETHOD(HRESULT, "_get_backgroundImage", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_backgroundRepeat", BSTR),
    STDMETHOD(HRESULT, "_get_backgroundRepeat", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_backgroundAttachment", BSTR),
    STDMETHOD(HRESULT, "_get_backgroundAttachment", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_backgroundPosition", BSTR),
    STDMETHOD(HRESULT, "_get_backgroundPosition", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_backgroundPositionX", VARIANT),
    STDMETHOD(HRESULT, "_get_backgroundPositionX", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_backgroundPositionY", VARIANT),
    STDMETHOD(HRESULT, "_get_backgroundPositionY", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_wordSpacing", VARIANT),
    STDMETHOD(HRESULT, "_get_wordSpacing", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_letterSpacing", VARIANT),
    STDMETHOD(HRESULT, "_get_letterSpacing", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_textDecoration", BSTR),
    STDMETHOD(HRESULT, "_get_textDecoration", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_textDecorationNone", c_int),
    STDMETHOD(HRESULT, "_get_textDecorationNone", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_textDecorationUnderline", c_int),
    STDMETHOD(HRESULT, "_get_textDecorationUnderline", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_textDecorationOverline", c_int),
    STDMETHOD(HRESULT, "_get_textDecorationOverline", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_textDecorationLineThrough", c_int),
    STDMETHOD(HRESULT, "_get_textDecorationLineThrough", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_textDecorationBlink", c_int),
    STDMETHOD(HRESULT, "_get_textDecorationBlink", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_verticalAlign", VARIANT),
    STDMETHOD(HRESULT, "_get_verticalAlign", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_textTransform", BSTR),
    STDMETHOD(HRESULT, "_get_textTransform", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_textAlign", BSTR),
    STDMETHOD(HRESULT, "_get_textAlign", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_textIndent", VARIANT),
    STDMETHOD(HRESULT, "_get_textIndent", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_lineHeight", VARIANT),
    STDMETHOD(HRESULT, "_get_lineHeight", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_marginTop", VARIANT),
    STDMETHOD(HRESULT, "_get_marginTop", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_marginRight", VARIANT),
    STDMETHOD(HRESULT, "_get_marginRight", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_marginBottom", VARIANT),
    STDMETHOD(HRESULT, "_get_marginBottom", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_marginLeft", VARIANT),
    STDMETHOD(HRESULT, "_get_marginLeft", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_margin", BSTR),
    STDMETHOD(HRESULT, "_get_margin", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_paddingTop", VARIANT),
    STDMETHOD(HRESULT, "_get_paddingTop", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_paddingRight", VARIANT),
    STDMETHOD(HRESULT, "_get_paddingRight", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_paddingBottom", VARIANT),
    STDMETHOD(HRESULT, "_get_paddingBottom", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_paddingLeft", VARIANT),
    STDMETHOD(HRESULT, "_get_paddingLeft", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_padding", BSTR),
    STDMETHOD(HRESULT, "_get_padding", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_border", BSTR),
    STDMETHOD(HRESULT, "_get_border", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderTop", BSTR),
    STDMETHOD(HRESULT, "_get_borderTop", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderRight", BSTR),
    STDMETHOD(HRESULT, "_get_borderRight", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderBottom", BSTR),
    STDMETHOD(HRESULT, "_get_borderBottom", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderLeft", BSTR),
    STDMETHOD(HRESULT, "_get_borderLeft", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderColor", BSTR),
    STDMETHOD(HRESULT, "_get_borderColor", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderTopColor", VARIANT),
    STDMETHOD(HRESULT, "_get_borderTopColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderRightColor", VARIANT),
    STDMETHOD(HRESULT, "_get_borderRightColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderBottomColor", VARIANT),
    STDMETHOD(HRESULT, "_get_borderBottomColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderLeftColor", VARIANT),
    STDMETHOD(HRESULT, "_get_borderLeftColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderWidth", BSTR),
    STDMETHOD(HRESULT, "_get_borderWidth", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderTopWidth", VARIANT),
    STDMETHOD(HRESULT, "_get_borderTopWidth", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderRightWidth", VARIANT),
    STDMETHOD(HRESULT, "_get_borderRightWidth", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderBottomWidth", VARIANT),
    STDMETHOD(HRESULT, "_get_borderBottomWidth", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderLeftWidth", VARIANT),
    STDMETHOD(HRESULT, "_get_borderLeftWidth", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_borderStyle", BSTR),
    STDMETHOD(HRESULT, "_get_borderStyle", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderTopStyle", BSTR),
    STDMETHOD(HRESULT, "_get_borderTopStyle", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderRightStyle", BSTR),
    STDMETHOD(HRESULT, "_get_borderRightStyle", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderBottomStyle", BSTR),
    STDMETHOD(HRESULT, "_get_borderBottomStyle", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_borderLeftStyle", BSTR),
    STDMETHOD(HRESULT, "_get_borderLeftStyle", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_width", VARIANT),
    STDMETHOD(HRESULT, "_get_width", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_height", VARIANT),
    STDMETHOD(HRESULT, "_get_height", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_styleFloat", BSTR),
    STDMETHOD(HRESULT, "_get_styleFloat", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_clear", BSTR),
    STDMETHOD(HRESULT, "_get_clear", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_display", BSTR),
    STDMETHOD(HRESULT, "_get_display", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_visibility", BSTR),
    STDMETHOD(HRESULT, "_get_visibility", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_listStyleType", BSTR),
    STDMETHOD(HRESULT, "_get_listStyleType", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_listStylePosition", BSTR),
    STDMETHOD(HRESULT, "_get_listStylePosition", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_listStyleImage", BSTR),
    STDMETHOD(HRESULT, "_get_listStyleImage", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_listStyle", BSTR),
    STDMETHOD(HRESULT, "_get_listStyle", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_whiteSpace", BSTR),
    STDMETHOD(HRESULT, "_get_whiteSpace", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_top", VARIANT),
    STDMETHOD(HRESULT, "_get_top", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_left", VARIANT),
    STDMETHOD(HRESULT, "_get_left", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_position", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_zIndex", VARIANT),
    STDMETHOD(HRESULT, "_get_zIndex", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_overflow", BSTR),
    STDMETHOD(HRESULT, "_get_overflow", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_pageBreakBefore", BSTR),
    STDMETHOD(HRESULT, "_get_pageBreakBefore", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_pageBreakAfter", BSTR),
    STDMETHOD(HRESULT, "_get_pageBreakAfter", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_cssText", BSTR),
    STDMETHOD(HRESULT, "_get_cssText", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_pixelTop", c_long),
    STDMETHOD(HRESULT, "_get_pixelTop", POINTER(c_long)),
    STDMETHOD(HRESULT, "_put_pixelLeft", c_long),
    STDMETHOD(HRESULT, "_get_pixelLeft", POINTER(c_long)),
    STDMETHOD(HRESULT, "_put_pixelWidth", c_long),
    STDMETHOD(HRESULT, "_get_pixelWidth", POINTER(c_long)),
    STDMETHOD(HRESULT, "_put_pixelHeight", c_long),
    STDMETHOD(HRESULT, "_get_pixelHeight", POINTER(c_long)),
    STDMETHOD(HRESULT, "_put_posTop", c_float),
    STDMETHOD(HRESULT, "_get_posTop", POINTER(c_float)),
    STDMETHOD(HRESULT, "_put_posLeft", c_float),
    STDMETHOD(HRESULT, "_get_posLeft", POINTER(c_float)),
    STDMETHOD(HRESULT, "_put_posWidth", c_float),
    STDMETHOD(HRESULT, "_get_posWidth", POINTER(c_float)),
    STDMETHOD(HRESULT, "_put_posHeight", c_float),
    STDMETHOD(HRESULT, "_get_posHeight", POINTER(c_float)),
    STDMETHOD(HRESULT, "_put_cursor", BSTR),
    STDMETHOD(HRESULT, "_get_cursor", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_clip", BSTR),
    STDMETHOD(HRESULT, "_get_clip", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_filter", BSTR),
    STDMETHOD(HRESULT, "_get_filter", POINTER(BSTR)),
    STDMETHOD(HRESULT, "setAttribute", BSTR, VARIANT, c_long),
    STDMETHOD(HRESULT, "getAttribute", BSTR, c_long, POINTER(VARIANT)),
    STDMETHOD(HRESULT, "removeAttribute", BSTR, c_long, POINTER(c_int)),
    STDMETHOD(HRESULT, "toString", POINTER(BSTR)),
]


IHTMLElementCollection._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "toString", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_length", c_long),
    STDMETHOD(HRESULT, "_get_length", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get__newEnum", POINTER(POINTER(IUnknown))),
    STDMETHOD(HRESULT, "item", VARIANT, VARIANT, POINTER(POINTER(IDispatch))),
    STDMETHOD(HRESULT, "tags", VARIANT, POINTER(POINTER(IDispatch))),
]


IHTMLElement._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "setAttribute", BSTR, VARIANT, c_long),
    STDMETHOD(HRESULT, "getAttribute", BSTR, c_long, POINTER(VARIANT)),
    STDMETHOD(HRESULT, "removeAttribute", BSTR, c_long, POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_className", BSTR),
    STDMETHOD(HRESULT, "_get_className", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_id", BSTR),
    STDMETHOD(HRESULT, "_get_id", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_tagName", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_parentElement", POINTER(POINTER(IHTMLElement))),
    STDMETHOD(HRESULT, "_get_style", POINTER(POINTER(IHTMLStyle))),
    STDMETHOD(HRESULT, "_put_onhelp", VARIANT),
    STDMETHOD(HRESULT, "_get_onhelp", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onclick", VARIANT),
    STDMETHOD(HRESULT, "_get_onclick", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_ondblclick", VARIANT),
    STDMETHOD(HRESULT, "_get_ondblclick", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onkeydown", VARIANT),
    STDMETHOD(HRESULT, "_get_onkeydown", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onkeyup", VARIANT),
    STDMETHOD(HRESULT, "_get_onkeyup", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onkeypress", VARIANT),
    STDMETHOD(HRESULT, "_get_onkeypress", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmouseout", VARIANT),
    STDMETHOD(HRESULT, "_get_onmouseout", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmouseover", VARIANT),
    STDMETHOD(HRESULT, "_get_onmouseover", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmousemove", VARIANT),
    STDMETHOD(HRESULT, "_get_onmousemove", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmousedown", VARIANT),
    STDMETHOD(HRESULT, "_get_onmousedown", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmouseup", VARIANT),
    STDMETHOD(HRESULT, "_get_onmouseup", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_document", POINTER(POINTER(IDispatch))),
    STDMETHOD(HRESULT, "_put_title", BSTR),
    STDMETHOD(HRESULT, "_get_title", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_language", BSTR),
    STDMETHOD(HRESULT, "_get_language", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_onselectstart", VARIANT),
    STDMETHOD(HRESULT, "_get_onselectstart", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "scrollIntoView", VARIANT),
    STDMETHOD(HRESULT, "contains", POINTER(IHTMLElement), POINTER(c_int)),
    STDMETHOD(HRESULT, "_get_sourceIndex", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_recordNumber", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_lang", BSTR),
    STDMETHOD(HRESULT, "_get_lang", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_offsetLeft", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_offsetTop", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_offsetWidth", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_offsetHeight", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_offsetParent", POINTER(POINTER(IHTMLElement))),
    STDMETHOD(HRESULT, "_put_innerHTML", BSTR),
    STDMETHOD(HRESULT, "_get_innerHTML", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_innerText", BSTR),
    STDMETHOD(HRESULT, "_get_innerText", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_outerHTML", BSTR),
    STDMETHOD(HRESULT, "_get_outerHTML", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_outerText", BSTR),
    STDMETHOD(HRESULT, "_get_outerText", POINTER(BSTR)),
    STDMETHOD(HRESULT, "insertAdjacentHTML", BSTR, BSTR),
    STDMETHOD(HRESULT, "insertAdjacentText", BSTR, BSTR),
    STDMETHOD(HRESULT, "_get_parentTextEdit", POINTER(POINTER(IHTMLElement))),
    STDMETHOD(HRESULT, "_get_isTextEdit", POINTER(c_int)),
    STDMETHOD(HRESULT, "click"),
    STDMETHOD(HRESULT, "_get_filters", POINTER(POINTER(IHTMLFiltersCollection))),
    STDMETHOD(HRESULT, "_put_ondragstart", VARIANT),
    STDMETHOD(HRESULT, "_get_ondragstart", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "toString", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_onbeforeupdate", VARIANT),
    STDMETHOD(HRESULT, "_get_onbeforeupdate", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onafterupdate", VARIANT),
    STDMETHOD(HRESULT, "_get_onafterupdate", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onerrorupdate", VARIANT),
    STDMETHOD(HRESULT, "_get_onerrorupdate", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onrowexit", VARIANT),
    STDMETHOD(HRESULT, "_get_onrowexit", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onrowenter", VARIANT),
    STDMETHOD(HRESULT, "_get_onrowenter", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_ondatasetchanged", VARIANT),
    STDMETHOD(HRESULT, "_get_ondatasetchanged", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_ondataavailable", VARIANT),
    STDMETHOD(HRESULT, "_get_ondataavailable", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_ondatasetcomplete", VARIANT),
    STDMETHOD(HRESULT, "_get_ondatasetcomplete", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onfilterchange", VARIANT),
    STDMETHOD(HRESULT, "_get_onfilterchange", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_children", POINTER(POINTER(IDispatch))),
    STDMETHOD(HRESULT, "_get_all", POINTER(POINTER(IDispatch))),
]


IHTMLDocument2._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "_get_Script", POINTER(POINTER(IDispatch))),
    STDMETHOD(HRESULT, "_get_all", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_get_body", POINTER(POINTER(IHTMLElement))),
    STDMETHOD(HRESULT, "_get_activeElement", POINTER(POINTER(IHTMLElement))),
    STDMETHOD(HRESULT, "_get_images", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_get_applets", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_get_links", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_get_forms", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_get_anchors", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_put_title", BSTR),
    STDMETHOD(HRESULT, "_get_title", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_scripts", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_put_designMode", BSTR),
    STDMETHOD(HRESULT, "_get_designMode", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_selection", POINTER(POINTER(IHTMLSelectionObject))),
    STDMETHOD(HRESULT, "_get_readyState", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_frames", POINTER(POINTER(IHTMLFramesCollection2))),
    STDMETHOD(HRESULT, "_get_embeds", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_get_plugins", POINTER(POINTER(IHTMLElementCollection))),
    STDMETHOD(HRESULT, "_put_alinkColor", VARIANT),
    STDMETHOD(HRESULT, "_get_alinkColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_bgColor", VARIANT),
    STDMETHOD(HRESULT, "_get_bgColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_fgColor", VARIANT),
    STDMETHOD(HRESULT, "_get_fgColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_linkColor", VARIANT),
    STDMETHOD(HRESULT, "_get_linkColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_vlinkColor", VARIANT),
    STDMETHOD(HRESULT, "_get_vlinkColor", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_get_referrer", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_location", POINTER(POINTER(IHTMLLocation))),
    STDMETHOD(HRESULT, "_get_lastModified", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_url", BSTR),
    STDMETHOD(HRESULT, "_get_url", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_domain", BSTR),
    STDMETHOD(HRESULT, "_get_domain", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_cookie", BSTR),
    STDMETHOD(HRESULT, "_get_cookie", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_expando", c_int),
    STDMETHOD(HRESULT, "_get_expando", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_charset", BSTR),
    STDMETHOD(HRESULT, "_get_charset", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_defaultCharset", BSTR),
    STDMETHOD(HRESULT, "_get_defaultCharset", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_mimeType", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_fileSize", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_fileCreatedDate", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_fileModifiedDate", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_fileUpdatedDate", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_security", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_protocol", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_get_nameProp", POINTER(BSTR)),
    STDMETHOD(HRESULT, "write", POINTER(SAFEARRAY)),
    STDMETHOD(HRESULT, "writeln", POINTER(SAFEARRAY)),
    STDMETHOD(HRESULT, "open", BSTR, VARIANT, VARIANT, VARIANT, POINTER(POINTER(IDispatch))),
    STDMETHOD(HRESULT, "close"),
    STDMETHOD(HRESULT, "clear"),
    STDMETHOD(HRESULT, "queryCommandSupported", BSTR, POINTER(c_int)),
    STDMETHOD(HRESULT, "queryCommandEnabled", BSTR, POINTER(c_int)),
    STDMETHOD(HRESULT, "queryCommandState", BSTR, POINTER(c_int)),
    STDMETHOD(HRESULT, "queryCommandIndeterm", BSTR, POINTER(c_int)),
    STDMETHOD(HRESULT, "queryCommandText", BSTR, POINTER(BSTR)),
    STDMETHOD(HRESULT, "queryCommandValue", BSTR, POINTER(VARIANT)),
    STDMETHOD(HRESULT, "execCommand", BSTR, c_int, VARIANT, POINTER(c_int)),
    STDMETHOD(HRESULT, "execCommandShowHelp", BSTR, POINTER(c_int)),
    STDMETHOD(HRESULT, "createElement", BSTR, POINTER(POINTER(IHTMLElement))),
    STDMETHOD(HRESULT, "_put_onhelp", VARIANT),
    STDMETHOD(HRESULT, "_get_onhelp", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onclick", VARIANT),
    STDMETHOD(HRESULT, "_get_onclick", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_ondblclick", VARIANT),
    STDMETHOD(HRESULT, "_get_ondblclick", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onkeyup", VARIANT),
    STDMETHOD(HRESULT, "_get_onkeyup", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onkeydown", VARIANT),
    STDMETHOD(HRESULT, "_get_onkeydown", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onkeypress", VARIANT),
    STDMETHOD(HRESULT, "_get_onkeypress", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmouseup", VARIANT),
    STDMETHOD(HRESULT, "_get_onmouseup", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmousedown", VARIANT),
    STDMETHOD(HRESULT, "_get_onmousedown", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmousemove", VARIANT),
    STDMETHOD(HRESULT, "_get_onmousemove", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmouseout", VARIANT),
    STDMETHOD(HRESULT, "_get_onmouseout", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onmouseover", VARIANT),
    STDMETHOD(HRESULT, "_get_onmouseover", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onreadystatechange", VARIANT),
    STDMETHOD(HRESULT, "_get_onreadystatechange", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onafterupdate", VARIANT),
    STDMETHOD(HRESULT, "_get_onafterupdate", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onrowexit", VARIANT),
    STDMETHOD(HRESULT, "_get_onrowexit", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onrowenter", VARIANT),
    STDMETHOD(HRESULT, "_get_onrowenter", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_ondragstart", VARIANT),
    STDMETHOD(HRESULT, "_get_ondragstart", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onselectstart", VARIANT),
    STDMETHOD(HRESULT, "_get_onselectstart", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "elementFromPoint", c_long, c_long, POINTER(POINTER(IHTMLElement))),
    STDMETHOD(HRESULT, "_get_parentWindow", POINTER(POINTER(IHTMLWindow2))),
    STDMETHOD(HRESULT, "_get_styleSheets", POINTER(POINTER(IHTMLStyleSheetsCollection))),
    STDMETHOD(HRESULT, "_put_onbeforeupdate", VARIANT),
    STDMETHOD(HRESULT, "_get_onbeforeupdate", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "_put_onerrorupdate", VARIANT),
    STDMETHOD(HRESULT, "_get_onerrorupdate", POINTER(VARIANT)),
    STDMETHOD(HRESULT, "toString", POINTER(BSTR)),
    STDMETHOD(HRESULT, "createStyleSheet", BSTR, c_long, POINTER(POINTER(IHTMLStyleSheet))),
]