
//Supression des doublons dans la liste des maladies presentes

function tri(selectID) {
    var query = "#" + selectID + " option";
    var map = {};
    $(query).each(function () {
        if (map[this.text]) {
            $(this).remove()
        }
        map[this.text] = true;
    })
}
//Mise dans l'ordre aplhabetique des choix possibe
function sort(selectID) {
    var query = "#" + selectID + " option";

    var options = $(query)
    var arr = options.map(function (_, o) {
        return {
            t: $(o).text(),
            v: o.value
        };
    }).get();
    arr.sort(function (o1, o2) {
        return o1.t > o2.t ? 1 : o1.t < o2.t ? -1 : 0;
    });
    options.each(function (i, o) {
        console.log(i);
        o.value = arr[i].v;
        $(o).text(arr[i].t);
    });

}
// Recherche dans le tableau du phenotype d'interet
function recherche() {
    if ('{{ maladieID }}' != 0) {
        var input, filter, table, tr, td, i, txtValue;
        input = $("#shearch option:selected").text();
        filter = input.toUpperCase();
        table = document.getElementById("myTable");
        tr = table.getElementsByTagName("tr");

        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[0];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }
}


