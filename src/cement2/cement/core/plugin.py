"""Cement core plugins module."""

from zope import interface

from cement.core.backend import minimal_logger
from cement.core.exc import CementInterfaceError

log = minimal_logger(__name__)

def config_invariant(obj):
    invalid = []
    members = [
        '__init__',
        '__handler_label__',
        '__handler_type__',
        'load_plugin',
        'load_plugins',
        'enabled_plugins',
        ]
        
    for member in members:
        if not hasattr(obj, member):
            invalid.append(member)
    
    if invalid:
        raise CementInterfaceError, \
            "Invalid or missing: %s in %s" % (invalid, obj)
    
class IPluginHandler(interface.Interface):
    """
    This class defines the Plugin Handler Interface.  Classes that 
    implement this handler must provide the methods and attributes defined 
    below.
    
    """
    # internal mechanism for handler registration
    __handler_type__ = interface.Attribute('Handler Type Identifier')
    __handler_label__ = interface.Attribute('Handler Label Identifier')
    interface.invariant(config_invariant)
    
    def __init__(defaults, *args, **kw):
        """
        The __init__ function emplementation of Cement handlers acts as a 
        wrapper for initialization.  In general, the implementation simply
        need to accept the config object as its first argument.  If the 
        implementation subclasses from something else it will need to
        handle passing the proper args/keyword args to that classes __init__
        function, or you can easily just pass *args, **kw directly to it.
        
        Required Arguments:
        
            config
                 The application configuration object after it has been parsed
                and processed.  This is *not* a defaults dictionary, though
                some config handler implementations may work as a dict.
        
        
        Optional Arguments:
        
            *args
                Additional positional arguments.
                
            **kw
                Additional keyword arguments.
                
        Returns: n/a
        
        """
    
    def load_plugin(self, plugin_name):
        """
        Load a plugin whose name is 'plugin_name'.
        
        Required Arguments:
        
            plugin_name
                The name of the plugin to load.
                
        """
        
    def load_plugins(self, plugin_list):
        """
        Load all plugins from plugin_list.
        
        Required Arguments:
        
            plugin_list
                A list of plugin names to load.
        
        """

class CementPluginHandler(object):
    __handler_type__ = 'plugin'
    __handler_label__ = 'cement'
    interface.implements(IPluginHandler)
    enabled_plugins = []
    
    def __init__(self, config, *args, **kw):
        self.config = config
        self.enabled_plugins = []
        
    def load_plugin(self, plugin_name):
        pass
    
    def load_plugins(self, plugin_list):
        pass
        

    
    
    
    
    
    
        