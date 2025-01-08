#import "@preview/oxifmt:0.2.1": strfmt

#let data = yaml("metadata.yml")

#let template(doc) = [
  #set page(
    header: context {
      if counter(page).get().first() > 1 [
        #data.courseName
        #h(1fr)
        #data.studentEmail.join[\ #h(1fr)]
      ]
    },
    footer: context {
      if counter(page).get().first() > 1 [
        #data.courseCode
        #h(1fr)
        #context counter(page).display("1")
        #h(1fr)
        #data.courseworkTitle
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

#let getStudentNames(data) = {
  let studentNames = ()

  for index in range(0, data.studentFirstName.len()) {
    studentNames.push(strong(strfmt(
      "{} {} ({})",
      data.studentFirstName.at(index),
      data.studentLastName.at(index),
      data.studentEmail.at(index)
    )))
  }

  return studentNames.join("\n")
}
