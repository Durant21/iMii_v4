

function getUrlBase() {
    return 'http://localhost:6543/';
    //return 'http://www.dev1.proto21.com/';
}

function verifyUser() {
        var user = document.getElementById('user').value;

        var pw = document.getElementById('password').value;
        //alert(user + ":" + pw);
        $.ajax({
                    type: "GET",
                    url: getUrlBase() + "api/login?u=" + user + "&pw=" + pw,
                    contentType: "application/json",
                    dataType: "json",

                    beforeSend: function () {
                        //$('#Grid_People').jqGrid('clearGridData');
                        //SetBusy();
                    },

                    success: function (data) {
                        //SetNotBusy();
                        var jsonObj = data;

                        //write key to hidden tag

                        if (data.api_key) {
                                var hKey = document.getElementById('hKey');

                                if (data.api_key == 'none') {
                                    alert('Invalid user or password; no user with these credentials');
                                } else {
                                    hKey.value = data.api_key;

                                    var hKey1 = document.getElementById('hKey1');
                                    hKey1.value = data.api_key;

                                    setLogoutVisible('true');

                                    // set Login panel not visible
                                    var login = document.getElementById('login');
                                    login.style.display = "none";

                                    resetAllAnchors();
                                    resetAllButtons();

                                    var q = getCurrentPage(window.location.href);

                                    // redirect back to Home
                                    if (q == 'People') {
                                        resetBtnURL('btnHome','iMii','true');

                                    } else if (q == 'OurProjects') {
                                        resetBtnURL('btnOurProjects','OurProjects','true')
                                    } else {
                                        resetBtnURL('btnHome','iMii','true');
                                    };
                                }

                        } else {
                            alert('Invalid user or password; no user with these credentials');

                        }


                    },
                    loadComplete: function () {
                        //$("#Grid_People").jqGrid('setGridWidth', $(window).width(), true);
                    },

                    error: function (err) {
                        //$.unblockUI();
                        //SetNotBusy();
                        alert("Error verifying user:" + err.status + "    " + err.statusText);
                    }
        });
    }

function getHiddenKey1() {
        var btn = document.getElementById("btnPeople")

        //location.href='People?k=getHiddenKey()
        var hKey = document.getElementById('hKey');
        // hKey.value = data.api_key;
        if (hKey) {
            return hKey.value;
        } else {
            return "";
        }
}

var getParams1 = function (url) {
    var params = {};
    var parser = document.createElement('a');
    parser.href = url;
    //alert(url);
    var query = parser.search.substring(1);
    //alert(query);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        params[pair[0]] = decodeURIComponent(pair[1]);
    }
    return params;
};

function getCurrentPage(url) {

    if (url.includes("People")) {
        //alert('yes');
        return 'People';
    } else if (url.includes("OurProjects")) {
        //alert('no');
        return 'OurProjects';
    } else {
        return 'none';
    };
}

function resetBtnURL(btnName,targetPage,sAutoClick) {

    //alert(getHiddenKey());
    hKeyVal = getHiddenKey();
    aBtn = document.getElementById(btnName);
    if (aBtn) {
        //alert('resetting ' + btnName + ' to ' + hKeyVal)
        if (hKeyVal == 'NONE' || hKeyVal == 'undefined') {
            aBtn.setAttribute("onclick", "location.href='" + targetPage + "'");
        } else {
            aBtn.setAttribute("onclick", "location.href='" + targetPage + "?k=" + hKeyVal + "'");
        }

        if (sAutoClick == 'true') {
            aBtn.click();
        }
    } else {
        //alert('could not locate ' + btnName )
    }
}

function resetAnchorURL(btnName,targetPage,sAutoClick) {

    //alert(getHiddenKey());
    hKeyVal = getHiddenKey();
    aBtn = document.getElementById(btnName);
    if (aBtn) {
        //alert('resetting anchor ' + btnName + ' to ' + hKeyVal)
        if (hKeyVal == 'NONE' || hKeyVal == 'undefined') {
            aBtn.setAttribute("href", "" + targetPage);
        } else {
            aBtn.setAttribute("href", "" + targetPage + "?k=" + hKeyVal);
        }

        if (sAutoClick == 'true') {
            aBtn.click();
        }
    } else {
        //alert('could not locate ' + btnName )
    }
}

function resetAllAnchors() {
    resetAnchorURL('aDiscover','Discover','false');
    resetAnchorURL('aReclaim','Reclaim','false');
    resetAnchorURL('aMiningCycle','MiningCycle','false');
    resetAnchorURL('aPlan','Plan','false');
    resetAnchorURL('aMine','Mine','false');
}

function resetAllButtons() {
    resetBtnURL('btnPeople','People','false');
    resetBtnURL('btnCurricula','Curricula','false')
}