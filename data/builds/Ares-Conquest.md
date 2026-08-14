---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.63
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.19
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.58
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.57
  - name: Stampede
    pick_rate: 0.24
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.4
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.55
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.73
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.85
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.71
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.57
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.8
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.2
    alternates:
    - name: Medallion
      pick_rate: 0.07
      win_rate: 0.75
    - name: Rune
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.27
    win_rate: 0.6
  - name: Warrior's Axe
    pick_rate: 0.2
    win_rate: 0.55
  - name: Heroism
    pick_rate: 0.19
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-14'
  god_win_rate: 0.5909090909090909
  god_matches_won: 65
  god_matches_played: 110
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Gluttonous Grimoire, Shield of the Phoenix, Oni Hunter''s Garb, Erosion, Eye of
    Providence, Draconic Scale, Jotunn''s Revenge, Spectral Armor, Pharaoh''s Curse,
    Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone of Binding,
    The Crusher, Midgardian Mail, Eye of the Storm, Hydra''s Lament, Shogun''s Ofuda,
    Helm of Radiance, Magi''s Cloak, Runeforged Hammer, Prophetic Cloak, Gladiator''s
    Shield, Screeching Gargoyle, Ancile, Xibalban Effigy, Hide of the Nemean Lion,
    Void Shield, Doublet of Binding, Rod of Asclepius, Yogi''s Necklace, Hussar''s
    Wings.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.77
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.71
      pick: 0.12
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.17
      fit: 0.67
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Gluttonous Grimoire, Rod of Asclepius, Chandra''s
    Grace, Oni Hunter''s Garb, Erosion, Eye of Providence, Phoenix Feather, Jotunn''s
    Revenge, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Leviathan''s Hide,
    Blood-Bound Book, Bancroft''s Talon, Midgardian Mail, Glorious Pridwen, The Crusher,
    Lifebinder, Runeforged Hammer, Eye of the Storm, Shogun''s Ofuda, Shield Splitter,
    Hydra''s Lament, Riptalon, Gladiator''s Shield, Ancile, Yogi''s Necklace, The
    Reaper, Hide of the Nemean Lion, Void Shield, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.71
      pick: 0.12
      fit: 0.55
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.17
      fit: 0.65
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Jotunn''s Revenge, Soul Gem,
    Kinetic Cuirass, The Crusher, Amanita Charm, Berserker''s Shield, Stone of Binding,
    Screeching Gargoyle, Spear of the Magus, Void Shield, Oni Hunter''s Garb, The
    Cosmic Horror, Shield of the Phoenix, Void Stone, Spear of Desolation, Avenging
    Blade, Erosion, Eye of Providence, Spectral Armor, Obsidian Shard, Riptalon, Pharaoh''s
    Curse, Draconic Scale, Silverbranch Bow, Hydra''s Lament, The Reaper, Shield Splitter,
    Leviathan''s Hide, Mantle Of Discord, Helm of Radiance, Runeforged Hammer, Midgardian
    Mail, Shogun''s Ofuda, Heartseeker, Eye of the Storm, The World Stone.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.71
      pick: 0.12
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The
    Crusher, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda, Shield of
    the Phoenix, Hydra''s Lament, Silverbranch Bow, Tyrfing, Runeforged Hammer, Spectral
    Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of The Abyss, Draconic
    Scale, Helm of Radiance, Eye of the Storm, Leviathan''s Hide, Midgardian Mail,
    Yogi''s Necklace, Mantle Of Discord, Death Metal, Stone of Binding, Eros'' Bow,
    Dominance, Spear of the Magus, Damaru, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.71
      pick: 0.12
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.33
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire,
    Berserker''s Shield, Hydra''s Lament, Oni Hunter''s Garb, Screeching Gargoyle,
    Chronos'' Pendant, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s
    Shield, Erosion, Prophetic Cloak, Spectral Armor, Eye of Providence, Pharaoh''s
    Curse, Shield Splitter, Draconic Scale, Helm of Radiance, Runeforged Hammer, Gem
    of Focus, Totem of Death, Leviathan''s Hide, Eye of the Storm, Mantle Of Discord,
    Rod of Asclepius, Midgardian Mail, Stone of Binding, Spear of the Magus, Death
    Metal, Arondight, Jade Scepter, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.71
      pick: 0.12
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Gluttonous Grimoire, Shield of the Phoenix, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Draconic Scale, Jotunn''s Revenge, Spectral Armor,
    Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord,
    Stone of Binding, The Crusher, Midgardian Mail, Eye of the Storm, Hydra''s Lament,
    Shogun''s Ofuda, Helm of Radiance, Magi''s Cloak, Runeforged Hammer, Gladiator''s
    Shield, Screeching Gargoyle, Prophetic Cloak, Ancile, Xibalban Effigy, Hide of
    the Nemean Lion, Void Shield, Doublet of Binding, Rod of Asclepius, Yogi''s Necklace,
    Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.4
      pick: 0.22
      fit: 0.38
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.38
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.71
      pick: 0.12
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.67
  starter: *id001
---
