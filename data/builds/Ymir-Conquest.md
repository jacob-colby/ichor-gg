---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.26
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.53
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.54
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.58
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.46
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.61
    alternates:
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.51
  - name: Spirit Robe
    pick_rate: 0.06
    win_rate: 0.62
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.67
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.55
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.74
    alternates:
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.75
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.61
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.19
    win_rate: 0.53
  - name: Selflessness
    pick_rate: 0.16
    win_rate: 0.47
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-10'
  god_win_rate: 0.5238693467336684
  god_matches_won: 417
  god_matches_played: 796
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Erosion, Gluttonous
    Grimoire, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence, Draconic
    Scale, Hide of the Nemean Lion, Spectral Armor, Mantle Of Discord, Leviathan''s
    Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Soul
    Gem, Ancile, Xibalban Effigy, Gladiator''s Shield, Void Shield, Prophetic Cloak,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.53
      pick: 0.26
      fit: 0.72
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Chandra''s Grace,
    Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Hide of the Nemean
    Lion, Spectral Armor, Leviathan''s Hide, Blood-Bound Book, Lifebinder, Midgardian
    Mail, Bancroft''s Talon, Glorious Pridwen, Gladiator''s Shield, Ancile, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.35
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.53
      pick: 0.26
      fit: 0.7
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Soul Gem, Amanita Charm, Stone
    of Binding, Spear of the Magus, Screeching Gargoyle, Freya''s Tears, Void Shield,
    Oni Hunter''s Garb, The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear
    of Desolation, Erosion, Eye of Providence, Obsidian Shard, Spectral Armor, Draconic
    Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian Mail,
    Doom Orb.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.25
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.26
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Gluttonous Grimoire, Amanita Charm, Freya''s Tears,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral Armor, Erosion,
    Eye of Providence, Bracer of The Abyss, Draconic Scale, Helm of Radiance, Death
    Metal, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding,
    Yogi''s Necklace, Bragi''s Harp, Rod of Asclepius, Blood-Bound Book, Bancroft''s
    Talon, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.2
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.2
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Shield
    of the Phoenix, Amanita Charm, Soul Gem, Gluttonous Grimoire, Oni Hunter''s Garb,
    Screeching Gargoyle, Chronos'' Pendant, Chandra''s Grace, Gladiator''s Shield,
    Erosion, Spectral Armor, Spear of Desolation, Eye of Providence, Prophetic Cloak,
    Draconic Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Death Metal,
    Midgardian Mail, Mantle Of Discord, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.26
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Soul Gem,
    Freya''s Tears, Runeforged Hammer, Shield Splitter, Oni Hunter''s Garb, Pharaoh''s
    Curse, Golden Blade, Lernaean Bow, Eye of the Storm, Shield of the Phoenix, Death
    Metal, Erosion, Spectral Armor, Eye of Providence, Spear of the Magus, Damaru,
    The Reaper, Shogun''s Ofuda, Draconic Scale, Avenging Blade, The Cosmic Horror,
    Helm of Radiance, Leviathan''s Hide, Riptalon, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Tekko-Kagi, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.22
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.22
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Kinetic Cuirass, Berserker''s Shield, The Crusher, Amanita Charm, Soul Gem, Freya''s
    Tears, Spear of the Magus, Oni Hunter''s Garb, Death Metal, Hydra''s Lament, Runeforged
    Hammer, The Cosmic Horror, Shield Splitter, Helm of Radiance, Shield of the Phoenix,
    Pharaoh''s Curse, Spectral Armor, Erosion, Eye of the Storm, Spear of Desolation,
    Rod of Asclepius, Eye of Providence, Jade Scepter, Golden Blade, Obsidian Shard,
    Lernaean Bow, Draconic Scale, Chronos'' Pendant, Damaru, Leviathan''s Hide, Blood-Bound
    Book, The Reaper, Bancroft''s Talon, Bracer of The Abyss, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.22
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.3
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.22
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Erosion,
    Gluttonous Grimoire, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence,
    Draconic Scale, Spectral Armor, Mantle Of Discord, Leviathan''s Hide, Stone of
    Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Soul Gem, Ancile, Xibalban
    Effigy, Gladiator''s Shield, Void Shield, Hide of the Nemean Lion, Prophetic Cloak,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.26
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.53
      pick: 0.26
      fit: 0.72
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
---
