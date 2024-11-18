#let template(doc) = [
  #set page(
    header: context {
      if counter(page).get().first() > 1 [
        Computer Network Security
        #h(1fr)
        cr2007 \ #h(1fr) fm2020
      ]
    },
    footer: context {
      if counter(page).get().first() > 1 [
        F20CN
        #h(1fr)
        #context counter(page).display("1")
        #h(1fr)
        Coursework 2
      ] else [#context counter(page).display("1")]
    }
  )

  #set text(font: "Segoe UI")

  #show heading.where(): it => {
    text(weight: "semibold", it)
  }

  #set align(center)

  #show link: underline

  #show outline.entry.where(level: 1): it => {
    v(12pt, weak: true)
    text(it)
  }

  #show figure: set block(breakable: true)

  #doc
]