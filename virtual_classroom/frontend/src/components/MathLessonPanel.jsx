const lessons = [
  {
    title: 'Algebra: Quadratic Equations',
    description: 'Work through vertex form, factoring, and the quadratic formula.',
    steps: [
      'Review the standard quadratic form ax² + bx + c = 0',
      'Demonstrate completing the square to derive the quadratic formula',
      'Solve sample problems together and assign practice questions',
    ],
  },
  {
    title: 'Geometry: Circle Theorems',
    description: 'Explore arc lengths, sector areas, and angle relationships.',
    steps: [
      'Recall definitions of central and inscribed angles',
      'Illustrate examples using the whiteboard diagrams',
      'Discuss real-world applications with student participation',
    ],
  },
  {
    title: 'Calculus: Derivatives',
    description: 'Introduce limits, derivative rules, and rate-of-change problems.',
    steps: [
      'Define the limit definition of a derivative',
      'Derive product, quotient, and chain rules using examples',
      'Assign differentiated practice problems for homework',
    ],
  },
];

const MathLessonPanel = () => (
  <div>
    <h2 className="section-title">Lesson Plan Highlights</h2>

    <div className="lesson-cards">
      {lessons.map(lesson => (
        <article key={lesson.title} className="lesson-card">
          <h3>{lesson.title}</h3>
          <p>{lesson.description}</p>
          <ul>
            {lesson.steps.map(step => (
              <li key={step}>{step}</li>
            ))}
          </ul>
        </article>
      ))}
    </div>
  </div>
);

export default MathLessonPanel;