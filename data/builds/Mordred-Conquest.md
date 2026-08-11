---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.58
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.53
    - name: Bracer of The Abyss
      pick_rate: 0.05
      win_rate: 0.52
  - name: Shield of the Phoenix
    pick_rate: 0.22
    win_rate: 0.62
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.15
      win_rate: 0.56
    - name: Gladiator's Shield
      pick_rate: 0.13
      win_rate: 0.68
  - name: Dwarven Plate
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.63
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.58
  - name: Kinetic Cuirass
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.58
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.6
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.59
    - name: Medal of Defense
      pick_rate: 0.04
      win_rate: 0.42
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.47
    win_rate: 0.66
  - name: Bluestone Pendant
    pick_rate: 0.34
    win_rate: 0.48
  - name: Bumba's Spear
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-10'
  god_win_rate: 0.5705378020265004
  god_matches_won: 732
  god_matches_played: 1283
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Gladiator's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Gluttonous Grimoire,
    Jotunn''s Revenge, Eye of Providence, The Crusher, Hide of the Nemean Lion, Oni
    Hunter''s Garb, Runeforged Hammer, Freya''s Tears, Breastplate of Valor, Shield
    Splitter, Hydra''s Lament, Soul Gem, Eye of the Storm, Erosion, Spectral Armor,
    Draconic Scale, Pharaoh''s Curse, Yogi''s Necklace, Avenging Blade, Death Metal,
    Golden Blade, Leviathan''s Hide, Spear of the Magus, Midgardian Mail, Lernaean
    Bow, Helm of Radiance, The Reaper, Mantle Of Discord, Stone of Binding, Damaru,
    Rod of Asclepius, Shogun''s Ofuda, The Cosmic Horror, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.28
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.61
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.43
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.68
      pick: 0.13
      fit: 0.53
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.51
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Gladiator's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, Soul Gem, The Crusher,
    Amanita Charm, Berserker''s Shield, Eye of Providence, Breastplate of Valor, Hydra''s
    Lament, Freya''s Tears, Oni Hunter''s Garb, Spear of the Magus, Runeforged Hammer,
    Spear of Desolation, The Cosmic Horror, Death Metal, Shield Splitter, Helm of
    Radiance, Rod of Asclepius, Spectral Armor, Yogi''s Necklace, Erosion, Eye of
    the Storm, Obsidian Shard, Pharaoh''s Curse, The Reaper, Chronos'' Pendant, Jade
    Scepter, Draconic Scale, Avenging Blade, Leviathan''s Hide, Golden Blade, Lernaean
    Bow, Damaru, Heartseeker, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.27
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.48
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.38
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.41
      win: 0.68
      pick: 0.13
      fit: 0.48
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Soul Gem, Gluttonous Grimoire, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Eye of Providence, Rod of Asclepius, The
    Reaper, Runeforged Hammer, Hide of the Nemean Lion, Oni Hunter''s Garb, Chandra''s
    Grace, Hydra''s Lament, Breastplate of Valor, Freya''s Tears, Eye of the Storm,
    Shield Splitter, Riptalon, Phoenix Feather, Spectral Armor, Erosion, Blood-Bound
    Book, Yogi''s Necklace, Bancroft''s Talon, Avenging Blade, Pharaoh''s Curse, Lifebinder,
    Golden Blade, Draconic Scale, Death Metal, Leviathan''s Hide, Midgardian Mail,
    Spear of the Magus, Lernaean Bow, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.25
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.6
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.74
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.68
      pick: 0.13
      fit: 0.54
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Soul Gem, Avenging Blade, Eye of Providence,
    Stone of Binding, Oni Hunter''s Garb, Runeforged Hammer, Screeching Gargoyle,
    Breastplate of Valor, Hydra''s Lament, Void Shield, Freya''s Tears, Spear of the
    Magus, Shield Splitter, The Reaper, Void Stone, The Cosmic Horror, Spectral Armor,
    Eye of the Storm, Spear of Desolation, Erosion, Heartseeker, Yogi''s Necklace,
    Pharaoh''s Curse, Draconic Scale, Riptalon, Obsidian Shard, Death Metal, Golden
    Blade, Leviathan''s Hide, Silverbranch Bow, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.52
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.35
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Riptalon
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Berserker''s Shield, Gluttonous Grimoire, Amanita Charm,
    The Crusher, Golden Blade, Eye of Providence, Jotunn''s Revenge, Riptalon, Pharaoh''s
    Curse, Oni Hunter''s Garb, Soul Gem, Breastplate of Valor, Runeforged Hammer,
    Freya''s Tears, Lernaean Bow, Hydra''s Lament, Silverbranch Bow, Shogun''s Ofuda,
    Tyrfing, Yogi''s Necklace, Bracer of The Abyss, Spectral Armor, Shield Splitter,
    Erosion, Spear of the Magus, Eye of the Storm, Dominance, Death Metal, Draconic
    Scale, Leviathan''s Hide, Rod of Asclepius, Helm of Radiance, The Reaper, Avenging
    Blade, Toxic Blade, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.19
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.44
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.28
    Riptalon:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Gladiator''s Shield,
    Jotunn''s Revenge, Soul Gem, Breastplate of Valor, Gluttonous Grimoire, Freya''s
    Tears, Amanita Charm, Berserker''s Shield, Hydra''s Lament, Eye of Providence,
    The Crusher, Hide of the Nemean Lion, Oni Hunter''s Garb, Spear of Desolation,
    Runeforged Hammer, Chronos'' Pendant, Screeching Gargoyle, Chandra''s Grace, Spectral
    Armor, Erosion, Shield Splitter, Yogi''s Necklace, Spear of the Magus, Pharaoh''s
    Curse, Helm of Radiance, Draconic Scale, Rod of Asclepius, Prophetic Cloak, Gem
    of Focus, Eye of the Storm, Death Metal, The Cosmic Horror, Leviathan''s Hide,
    Arondight, Jade Scepter, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.51
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.56
    Gladiator's Shield:
      total: 0.56
      efficiency: 0.41
      win: 0.68
      pick: 0.13
      fit: 0.66
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Gladiator's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Kinetic Cuirass, Gluttonous Grimoire, Soul
    Gem, Amanita Charm, Jotunn''s Revenge, Berserker''s Shield, The Crusher, Eye of
    Providence, Breastplate of Valor, Oni Hunter''s Garb, Hydra''s Lament, Freya''s
    Tears, Runeforged Hammer, Spear of the Magus, Death Metal, The Cosmic Horror,
    Helm of Radiance, Rod of Asclepius, Spear of Desolation, Shield Splitter, Jade
    Scepter, Spectral Armor, Chronos'' Pendant, Yogi''s Necklace, Eye of the Storm,
    Erosion, Obsidian Shard, Pharaoh''s Curse, Wish-Granting Pearl, Blood-Bound Book,
    Draconic Scale, Ethereal Staff, Triton''s Conch, Bancroft''s Talon, Avenging Blade,
    Golden Blade, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.25
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.49
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.36
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.41
      win: 0.68
      pick: 0.13
      fit: 0.46
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Gladiator's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Gluttonous Grimoire,
    Amanita Charm, The Crusher, Jotunn''s Revenge, Berserker''s Shield, Soul Gem,
    Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament, Breastplate
    of Valor, Death Metal, Freya''s Tears, Spear of the Magus, Shield Splitter, The
    Cosmic Horror, Helm of Radiance, Rod of Asclepius, Eye of the Storm, Spectral
    Armor, Erosion, Spear of Desolation, Jade Scepter, Yogi''s Necklace, Pharaoh''s
    Curse, Avenging Blade, Draconic Scale, Golden Blade, Obsidian Shard, Lernaean
    Bow, The Reaper, Triton''s Conch, Chronos'' Pendant, Damaru, Leviathan''s Hide,
    Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.23
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.52
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.22
      fit: 0.35
    Gladiator's Shield:
      total: 0.52
      efficiency: 0.41
      win: 0.68
      pick: 0.13
      fit: 0.45
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Berserker''s Shield,
    Gluttonous Grimoire, Jotunn''s Revenge, Eye of Providence, The Crusher, Oni Hunter''s
    Garb, Runeforged Hammer, Freya''s Tears, Breastplate of Valor, Shield Splitter,
    Hydra''s Lament, Soul Gem, Eye of the Storm, Erosion, Spectral Armor, Draconic
    Scale, Pharaoh''s Curse, Yogi''s Necklace, Avenging Blade, Death Metal, Golden
    Blade, Leviathan''s Hide, Spear of the Magus, Midgardian Mail, Lernaean Bow, Helm
    of Radiance, The Reaper, Mantle Of Discord, Stone of Binding, Hide of the Nemean
    Lion, Damaru, Rod of Asclepius, Shogun''s Ofuda, The Cosmic Horror, Stampede.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.17
      fit: 0.28
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.65
      pick: 0.06
      fit: 0.61
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
---
