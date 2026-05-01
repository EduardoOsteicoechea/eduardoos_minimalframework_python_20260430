PAGE_ACTIONS_STYLES = """

.page_actions_button{
    height: 45px;
    width: 45px;
    border-radius: 4px;
    border:none;
    position: fixed;
    bottom:10px;
    right:10px;
    cursor:pointer;
    z-index: 10000;
}
.page_actions_button_active{
    background: var(--button_active);
}
.page_actions_button_unactive{
}
.page_actions_main_container{
    display: none;
    align-items: center;
    gap: 10px;
    padding: 0 10px;
    height:50px;
    overflow: auto;
    width: 70vw;
    position: fixed;
    bottom:65px;
    right:20px;
    background: #fff;
    box-shadow: 10px 10px 15px rgba(0,0,0,.15);
    border-radius:4px;
    z-index: 9000;
}
.page_action_button{    
    height: 35px;
    width: 35px;
    border-radius: 4px;
    z-index: 10000;
}

"""
 