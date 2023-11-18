//
//  ParagraphItem.swift
//  MediCat
//
//  Created by Nikolas Psathakis on 18.11.23.
//

import Foundation

struct ParagraphItem: Codable, Identifiable {
    let id = UUID()
    let original_paragraph: String
    let category_id: Int
    let paragraph_number: String
    let relevance_score: Double

    enum CodingKeys: String, CodingKey {
        case original_paragraph
        case category_id
        case paragraph_number
        case relevance_score
    }
}
