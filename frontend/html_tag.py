from typing import Optional
from frontend.html_sanitize import html_sanitize

def html_tag(
   tag_name: str, 
   tag_content: Optional[list[str]] = None, 
   tag_attributes: Optional[dict[str, str]] = None
   ) -> str:
    
    safe_content = tag_content or []
    safe_attrs = tag_attributes or {}
    
    joined_content = "".join([str(item) for item in safe_content])
    
    attr_list = []
    
    for key, value in safe_attrs.items():
        attr_name = "class" if key == "class_" else key.replace("_", "-")
        attr_list.append(f'{attr_name}="{html_sanitize(value)}"')
    
    attr_str = f" {' '.join(attr_list)}" if attr_list else ""
    
    return f"<{tag_name}{attr_str}>{joined_content}</{tag_name}>"