---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.37
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.26
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.67
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.17
    win_rate: 0.42
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.2
  - name: Spirit Robe
    pick_rate: 0.11
    win_rate: 0.71
    alternates:
    - name: Stone of Binding
      pick_rate: 0.08
      win_rate: 0.8
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Adroit Ring
      pick_rate: 0.06
      win_rate: 0.33
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.33
  - name: Engraved Guard
    pick_rate: 0.26
    win_rate: 0.67
    alternates:
    - name: Stygian Anchor
      pick_rate: 0.09
      win_rate: 1.0
    - name: Oracle Staff
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Selflessness
    pick_rate: 0.3
    win_rate: 0.43
  - name: Heroism
    pick_rate: 0.13
    win_rate: 0.67
  - name: War Flag
    pick_rate: 0.12
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-08-13'
  god_win_rate: 0.43478260869565216
  god_matches_won: 30
  god_matches_played: 69
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Stone of Binding, Freya''s Tears, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Shield of the Phoenix, Shifter''s Shield, Oni Hunter''s Garb, Erosion,
    Eye of Providence, Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord,
    Leviathan''s Hide, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Prophetic Cloak, Screeching Gargoyle, Ancile, Xibalban Effigy, Hide of
    the Nemean Lion, Void Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.62
      efficiency: 0.48
      win: 0.8
      pick: 0.13
      fit: 0.6
    Stygian Anchor:
      total: 0.68
      efficiency: 0.42
      win: 1.0
      pick: 0.28
      fit: 0.5
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.65
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.7
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Breastplate of Valor
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Chandra''s Grace, Oni Hunter''s
    Garb, Shifter''s Shield, Erosion, Eye of Providence, Phoenix Feather, Draconic
    Scale, Spectral Armor, Blood-Bound Book, Leviathan''s Hide, Bancroft''s Talon,
    Lifebinder, Glorious Pridwen, Midgardian Mail, Gladiator''s Shield, Ancile, Jade
    Scepter, Helm of Radiance.'
  slot_scores:
    Stone of Binding:
      total: 0.61
      efficiency: 0.48
      win: 0.8
      pick: 0.13
      fit: 0.52
    Stygian Anchor:
      total: 0.67
      efficiency: 0.42
      win: 1.0
      pick: 0.28
      fit: 0.42
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.37
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.58
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Stone of Binding, Gluttonous Grimoire, Freya''s Tears, Soul Gem,
    Kinetic Cuirass, Amanita Charm, Screeching Gargoyle, Spear of the Magus, Void
    Shield, The Cosmic Horror, Oni Hunter''s Garb, Shield of the Phoenix, Spear of
    Desolation, Void Stone, Shifter''s Shield, Erosion, Obsidian Shard, Eye of Providence,
    Spectral Armor, Draconic Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of
    Discord, Midgardian Mail, The World Stone.'
  slot_scores:
    Stone of Binding:
      total: 0.65
      efficiency: 0.48
      win: 0.8
      pick: 0.13
      fit: 0.75
    Stygian Anchor:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.28
      fit: 0.35
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Stone of Binding, Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Oni Hunter''s Garb, Shield of the Phoenix, Spectral Armor,
    Shifter''s Shield, Erosion, Bracer of The Abyss, Eye of Providence, Helm of Radiance,
    Draconic Scale, Leviathan''s Hide, Death Metal, Midgardian Mail, Yogi''s Necklace,
    Mantle Of Discord, Spear of the Magus, Blood-Bound Book, Rod of Asclepius, Bragi''s
    Harp, Bancroft''s Talon.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.48
      win: 0.8
      pick: 0.13
      fit: 0.36
    Stygian Anchor:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.28
      fit: 0.26
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Shield
    of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s Garb,
    Screeching Gargoyle, Spear of Desolation, Chandra''s Grace, Gladiator''s Shield,
    Shifter''s Shield, Erosion, Spectral Armor, Prophetic Cloak, Eye of Providence,
    Draconic Scale, Helm of Radiance, Gem of Focus, Totem of Death, Leviathan''s Hide,
    Chronos'' Pendant, Mantle Of Discord, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.6
      efficiency: 0.48
      win: 0.8
      pick: 0.13
      fit: 0.42
    Stygian Anchor:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.28
      fit: 0.32
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.28
      fit: 0.48
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Stone of Binding, Freya''s Tears, Jotunn''s
    Revenge, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Hydra''s Lament, Oni Hunter''s Garb, Runeforged Hammer,
    Shield Splitter, Pharaoh''s Curse, Golden Blade, Shield of the Phoenix, Lernaean
    Bow, Eye of the Storm, Shifter''s Shield, Death Metal, Erosion, Spectral Armor,
    Spear of the Magus, Eye of Providence, Damaru, Shogun''s Ofuda, Draconic Scale,
    The Reaper, The Cosmic Horror, Avenging Blade, Helm of Radiance, Riptalon, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Spear of Desolation, Heartseeker, Silverbranch
    Bow, Yogi''s Necklace.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.48
      win: 0.8
      pick: 0.13
      fit: 0.39
    Stygian Anchor:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.28
      fit: 0.29
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Stone of Binding
  - Stygian Anchor
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Soul Gem, Amanita Charm, Berserker''s
    Shield, Spear of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death Metal,
    The Cosmic Horror, Shield of the Phoenix, Runeforged Hammer, Helm of Radiance,
    Shield Splitter, Spear of Desolation, Shifter''s Shield, Erosion, Spectral Armor,
    Eye of the Storm, Rod of Asclepius, Eye of Providence, Pharaoh''s Curse, Jade
    Scepter, Obsidian Shard, Draconic Scale, Golden Blade, Leviathan''s Hide, Blood-Bound
    Book, Damaru, Lernaean Bow, Bancroft''s Talon, The Reaper, Ethereal Staff, Midgardian
    Mail, Wish-Granting Pearl, Chronos'' Pendant.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.48
      win: 0.8
      pick: 0.13
      fit: 0.39
    Stygian Anchor:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.28
      fit: 0.29
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Shield of the Phoenix, Shifter''s Shield, Oni Hunter''s Garb, Erosion,
    Eye of Providence, Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord,
    Leviathan''s Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s
    Cloak, Gladiator''s Shield, Prophetic Cloak, Screeching Gargoyle, Ancile, Xibalban
    Effigy, Hide of the Nemean Lion, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.28
      fit: 0.4
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.63
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.65
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.7
  starter: *id001
---
