//
//  FeedViewModel.swift
//  MediCat
//
//  Created by Nikolas Psathakis on 18.11.23.
//

import Foundation

class FeedViewModel: ObservableObject {
    @Published var items: [ParagraphItem] = []

    init() {
        loadItems()
    }

    func loadItems() {
        guard let url = Bundle.main.url(forResource: "example", withExtension: "json"),
              let data = try? Data(contentsOf: url) else {
            print("Failed to load example.json from bundle.")
            return
        }

        do {
            items = try JSONDecoder().decode([ParagraphItem].self, from: data)
            items.sort { $0.relevance_score > $1.relevance_score }
        } catch {
            print("Error parsing JSON: \(error)")
        }
    }
}
